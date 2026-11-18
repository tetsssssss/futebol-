import struct,sys
A='http://schemas.android.com/apk/res/android'
ID={'versionCode':0x0101021b,'versionName':0x0101021c,'minSdkVersion':0x0101020c,'targetSdkVersion':0x01010270,'label':0x01010001,'name':0x01010003,'exported':0x01010010,'configChanges':0x0101001f,'hardwareAccelerated':0x010102d3,'allowBackup':0x01010280,'windowSoftInputMode':0x0101022b}
# árvore: (tag, [(attr, tipo, valor)], [filhos]); tipo: s=string i=int h=hex b=bool
def build(root,out):
    strings=[];resattrs=sorted({a for a in ID},key=lambda k:ID[k])
    used=set()
    def walk(n):
        for k,t,v in n[1]:
            if k in ID:used.add(k)
        for c in n[2]:walk(c)
    walk(root)
    ordered=[k for k in resattrs if k in used]
    def sid(s):
        if s not in strings:strings.append(s)
        return strings.index(s)
    for k in ordered:sid(k)
    nres=len(ordered)
    sid('android');sid(A)
    def walk2(n):
        sid(n[0])
        for k,t,v in n[1]:
            sid(k)
            if t=='s':sid(v)
        for c in n[2]:walk2(c)
    walk2(root)
    def pool():
        body=b'';offs=[]
        for s in strings:
            offs.append(len(body));b=s.encode('utf-16-le');assert len(s)<0x7fff
            body+=struct.pack('<H',len(s))+b+b'\0\0'
        while len(body)%4:body+=b'\0'
        hs=28;start=hs+4*len(strings)
        return struct.pack('<HHIIIIII',1,hs,start+len(body),len(strings),0,0,start,0)+b''.join(struct.pack('<I',o) for o in offs)+body
    resmap=struct.pack('<HHI',0x180,8,8+4*nres)+b''.join(struct.pack('<I',ID[k]) for k in ordered)
    NO=0xFFFFFFFF
    body=struct.pack('<HHIIIII',0x100,16,24,1,NO,sid('android'),sid(A))
    def emit(n):
        nonlocal body
        attrs=[]
        for k,t,v in n[1]:
            if k in ID:ns=sid(A);rid=ID[k]
            else:ns=NO;rid=0xFFFFFFFF
            if t=='s':raw=sid(v);typ=3;data=raw
            elif t=='i':raw=NO;typ=0x10;data=v
            elif t=='h':raw=NO;typ=0x11;data=v
            else:raw=NO;typ=0x12;data=0xFFFFFFFF if v else 0
            attrs.append((rid,ns,sid(k),raw,typ,data))
        attrs.sort(key=lambda a:a[0])
        body+=struct.pack('<HHIIIIIHHHHHH',0x102,16,36+20*len(attrs),1,NO,NO,sid(n[0]),0x14,0x14,len(attrs),0,0,0)
        for rid,ns,nm,raw,typ,data in attrs:body+=struct.pack('<IIIHBBI',ns,nm,raw,8,0,typ,data)
        for c in n[2]:emit(c)
        body+=struct.pack('<HHIIIII',0x103,16,24,1,NO,NO,sid(n[0]))
    emit(root)
    body+=struct.pack('<HHIIIII',0x101,16,24,1,NO,sid('android'),sid(A))
    p=pool()
    chunks=p+resmap+body
    open(out,'wb').write(struct.pack('<HHI',3,8,8+len(chunks))+chunks)
if __name__=='__main__':
    pkg='com.footballuniverse.treinador'
    act=('activity',[('name','s','.MainActivity'),('exported','b',True),('configChanges','h',0x1fb0),('windowSoftInputMode','h',0x10)],
        [('intent-filter',[],[('action',[('name','s','android.intent.action.MAIN')],[]),('category',[('name','s','android.intent.category.LAUNCHER')],[])])])
    root=('manifest',[('versionCode','i',1),('versionName','s','0.15.0-modernizacao'),('package','s',pkg)],[
      ('uses-sdk',[('minSdkVersion','i',24),('targetSdkVersion','i',33)],[]),
      ('uses-permission',[('name','s','android.permission.INTERNET')],[]),
      ('application',[('label','s','Football Universe'),('allowBackup','b',False),('hardwareAccelerated','b',True)],[act])])
    build(root,sys.argv[1])
