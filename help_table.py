import glob

images = glob.glob('./images/nodes/definitions/*.png')

images.sort()

nodes = ['goal','weight', 'diet', 'sleep', 'rest', 'sex', 'genetic', 'body fat', 'gains', 'hormones', '1RM']

def render_section(node, image):

  return "### {}\n{}\n".format(node, render_image(image))

def render_image(image):
  return "![alt]({})".format(image)

rendered = ''

for node, image in zip(nodes, images):
  rendered += render_section(node, image)

print(rendered)

