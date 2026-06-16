from pathlib import Path
import re

path = Path('index.html')
content = path.read_text(encoding='utf-8')

# Remove external Google Font references
content = content.replace(
    '<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; base-uri \'self\'; img-src \'self\' data:; style-src \'self\' \'unsafe-inline\' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; script-src \'self\' \'unsafe-inline\'; form-action \'self\' mailto:; frame-ancestors \'self\'" />',
    '<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; base-uri \'self\'; img-src \'self\' data:; style-src \'self\' \'unsafe-inline\'; font-src \'self\'; script-src \'self\' \'unsafe-inline\'; form-action \'self\' mailto:; frame-ancestors \'self\'" />'
)
content = re.sub(r"(?m)^<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />\r?\n?", '', content)
content = re.sub(r"(?m)^<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />\r?\n?", '', content)
content = re.sub(r"(?m)^<link href=\"https://fonts.googleapis.com/css2[^\n]*\" rel=\"stylesheet\" />\r?\n?", '', content)

# Use system font fallback instead of external fonts
content = content.replace('    --font-display: "Fraunces", Georgia, "Times New Roman", serif;', '    --font-display: Georgia, "Times New Roman", serif;')
content = content.replace('    --font-body: "Hanken Grotesk", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;', '    --font-body: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;')

# Replace the favicon with an inline SVG favicon
svg_icon = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2320453b'/%3E%3Cpath d='M12 44L28 24L40 38L52 20' fill='none' stroke='%23f7e0b5' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'/%3E%3Ccircle cx='52' cy='14' r='6' fill='%23b07d2e'/%3E%3C/svg%3E"
content = re.sub(r'<link rel="icon" href="data:image/png;base64[^"]+" />', f'<link rel="icon" href="{svg_icon}" />', content)

path.write_text(content, encoding='utf-8')
print('Updated index.html')
