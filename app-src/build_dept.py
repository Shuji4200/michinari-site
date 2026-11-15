s=open('index.html').read()
assert 'const APP_MODE="main";' in s
for k in ["ceo","cso","cmo","cpo","chro","cfo","clo","public"]:
  t=s.replace('const APP_MODE="main";',f'const APP_MODE="{k}";',1)
  if k=='public':t=t.replace('<meta name="viewport"','<meta name="robots" content="noindex">\n<meta name="viewport"',1)
  open(f'dept/{k}.html','w').write(t)
print("built")
