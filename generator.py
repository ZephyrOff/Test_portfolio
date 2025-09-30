import yaml
import os
from jinja2 import Environment, FileSystemLoader

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
    if "project" in context and "extra_markdown_content" in context['project']:
        context['project']['extra_markdown_content'] = read_markdown_file(context['project']['extra_markdown_content'])
    html = template.render(**context)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Généré : {output_path}")

print(f"\n🌍 Site généré dans : {output_dir}")
