import yaml
import os
import shutil
from jinja2 import Environment, FileSystemLoader
import base64
import mimetypes
import re

def image_to_base64(path):
    print(path)
    mime_type, _ = mimetypes.guess_type(path)
    if not mime_type:
        return None

    with open(path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"

def inline_obsidian_images(md, base_path="."):
    pattern = r'!\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'

    def replacer(match):
        filename = match.group(1).strip()

        if filename.startswith(("http://", "https://", "data:")):
            return match.group(0)

        img_path = os.path.join(base_path, filename)
        if not os.path.exists(img_path):
            return match.group(0)

        data_url = image_to_base64(img_path)
        if not data_url:
            return match.group(0)

        # Conversion vers Markdown standard
        return f'![]({data_url})'

    return re.sub(pattern, replacer, md)



def inline_images_in_markdown(md, base_path="."):
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'

    def replacer(match):
        alt = match.group(1)
        src = match.group(2)

        # ignorer URLs externes ou base64
        if src.startswith(("http://", "https://", "data:")):
            return match.group(0)

        img_path = os.path.join(base_path, src)
        if not os.path.exists(img_path):
            return match.group(0)

        data_url = image_to_base64(img_path)
        if not data_url:
            return match.group(0)

        return f'![{alt}]({data_url})'

    return re.sub(pattern, replacer, md)



def inline_images_in_html(html, base_path="."):
    pattern = r'<img[^>]+src=["\']([^"\']+)["\']'

    def replacer(match):
        src = match.group(1)

        # ignorer les URLs externes ou déjà en base64
        if src.startswith(("http://", "https://", "data:")):
            return match.group(0)

        img_path = os.path.join(base_path, src)

        if not os.path.exists(img_path):
            return match.group(0)

        data_url = image_to_base64(img_path)
        if not data_url:
            return match.group(0)

        return match.group(0).replace(src, data_url)

    return re.sub(pattern, replacer, html)


def read_markdown_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Charger la config YAML
with open("site.yml", "r", encoding="utf-8") as f:
    site = yaml.safe_load(f)

config = site["config"]
pages = site["pages"]

# Créer le dossier de sortie
output_dir = config.get("output_dir", "build")
os.makedirs(output_dir, exist_ok=True)

# Copier les fichiers statiques vers le build
static_src = "static"
static_dst = os.path.join(output_dir, "static")
if os.path.exists(static_src):
    if os.path.exists(static_dst):
        shutil.rmtree(static_dst)
    shutil.copytree(static_src, static_dst)

# Configurer Jinja2
env = Environment(loader=FileSystemLoader("templates"))
env.globals.update({
    "site_name": config.get("site_name"),
    "base_url": config.get("base_url"),
    "author": config.get("author"),
})

# Générer les pages
for page in pages:
    template_name = page.get("template", config.get("default_template"))
    output_path = os.path.join(output_dir, page["output"])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    template = env.get_template(template_name)
    context = page.get("context", {})

    context['theme'] = config.get("theme", {})
    context['custom_css'] = config.get("custom_css", {})
    if "content" in context:
        md = read_markdown_file(context['content'])
        md = inline_obsidian_images(md, base_path="content")
        md = inline_images_in_markdown(md, base_path="content")
        context["content"] = md

    if "data" in page:
        with open(page["data"], "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        for element_name, element in data.items():
            #print(element)
            context[element_name] = element

    html = template.render(**context)

    # 🔥 Conversion des images en base64
    html = inline_images_in_html(html, base_path="content")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Généré : {output_path}")

print(f"\n🌍 Site généré dans : {output_dir}")
