# Builds the Tilda blocks from index.html. Run: python3 tilda/build.py
import re,os
BASE='https://q-team-new-year-2027.vercel.app/'
H=os.path.dirname(os.path.abspath(__file__));s=open(os.path.join(H,'..','index.html'),encoding='utf-8').read()
fonts='\n'.join(re.findall(r'<link rel="(?:preconnect|stylesheet)"[^>]*>',s))
css=s[s.index('<style>')+7:s.index('</style>')].replace('url(img/','url('+BASE+'img/')
markup=s[s.index('<main id="stage">'):s.index('</main>')+7]
js=s[s.index('<script>')+8:s.rindex('</script>')]
data,app=js.split('\n',1) if js.startswith('\nconst D=') is False else (None,None)
k=js.index('(function(){');data=js[:k].strip();app=js[k:].strip()
out={'1-styles.html':fonts+'\n<style>'+css+'</style>\n',
     '2-markup.html':markup+'\n',
     '3-data.html':"<script>window.QTEAM_BASE='"+BASE+"';\n"+data+"\n</script>\n",
     '4-app.html':'<script>\n'+app+'\n</script>\n'}
for n,t in out.items():open(os.path.join(H,n),'w',encoding='utf-8').write(t);print(n,len(t.encode()))
# one-file alternative: everything hosted on Vercel, the Tilda block only links to it
open(os.path.join(H,'..','qteam.css'),'w',encoding='utf-8').write(css)
open(os.path.join(H,'..','qteam.js'),'w',encoding='utf-8').write("window.QTEAM_BASE=window.QTEAM_BASE||'"+BASE+"';\n"+data+'\n'+app+'\n')
open(os.path.join(H,'0-short-embed.html'),'w',encoding='utf-8').write(fonts+'\n<link rel="stylesheet" href="'+BASE+'qteam.css">\n'+markup+'\n<script src="'+BASE+'qteam.js"></script>\n')
print('0-short-embed.html',os.path.getsize(os.path.join(H,'0-short-embed.html')))
