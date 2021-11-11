# Инструменты гит

1. git log --pretty=format:"%H %s" | grep ^aefea

<code> aefead2207ef7e2aa5dc81a34aedf0cad4c32545 Update CHANGELOG.md </code>

2. git log --tags --oneline | grep 85024d3

<code>85024d310 v0.12.23 </code>

3. У коммита b8d720 2 родителя.  
git log --pretty=%p -n 1 b8d720

<code>56cd7859e 9ea88f22f </code>

5. git log v0.12.23..v0.12.24 --pretty="%h - %s"

<code>33ff1c03b - v0.12.24 \
14b74c49 - [Website] vmc provider links \
3f235065b - Update CHANGELOG.md \
6ae64e247 - registry: Fix panic when server is unreachable \
5c619ca1b - website: Remove links to the getting started guide's old location \
06275647e - Update CHANGELOG.md \
d5f9411f5 - command: Fix bug when using terraform login on Widows \
4b6d06cc5 - Update CHANGELOG.md \
dd01a3507 - Update CHANGELOG.md \
225466bc3 - Cleanup after v0.12.23 release</code> 

5. git log -S "func providerSource(" --pretty="%h", git show 8c928e835, что бы убедится, что именно в этом коммите была добавлена функция 

<code>8c928e835</code>
6. git grep -p "globalPluginDirs("  
git log -L :globalPluginDirs:plugins.go --pretty="hash= %h" | grep "hash="

<code>hash= 78b122055 \
hash= 52dbf9483 \
hash= 41ab0aef7 \
hash= 66ebff90c \
hash= 8364383c3 </code>

7. git log -S "func synchronizedWriters(" --pretty=format:"%an %s %ad"

<code>Martin Atkins </code>

