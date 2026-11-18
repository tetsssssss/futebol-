# APK do Football Universe (Modo Treinador) — build de teste

`FootballUniverse-treinador-debug.apk` (24 MB, SHA-256 `44b885d9a20ee78288e33d2cfb4bf609cb2cf07fc9cc063e77b9127cc57f6748`).

## O que é
Casca Android mínima (um `WebView`) que embute o código-fonte do jogo (`treinador/`, `copa/`, `src/`, `data/`, `assets/`, `architecture/`) e o serve numa origem https virtual (`appassets.footballuniverse.local`), sem servidor e sem rede. Abre em `treinador/index.html`. Os saves usam o IndexedDB do WebView. A CDN do Babylon (2.5D) só carrega com internet; sem ela o jogo cai no campo 2D.

## Instalar
Android 7.0+ (minSdk 24). Copie o arquivo para o celular, permita "instalar apps desconhecidos" e abra. Assinado com chave de depuração própria (v2), **não** é build para a Play Store.

## O que foi verificado
- Assinatura v2 validada com o verificador do apksig; ZIP íntegro; manifesto relido por parser independente (pacote `com.footballuniverse.treinador`, minSdk 24, targetSdk 33, atividade principal, permissão INTERNET).
- O conteúdo embutido, servido em raiz de origem num Chromium headless a 390 px, abre, cria campeonato, inicia e roda a partida sem erro de página nem 404.

## O que NÃO foi verificado
- **A APK não foi instalada nem executada em aparelho ou emulador** (o SDK/emulador do Android não está acessível neste ambiente). O manifesto binário e o DEX foram montados à mão, sem aapt2/Gradle. Se o instalador recusar ("pacote inválido") ou o app fechar ao abrir, me envie a mensagem/`adb logcat`.
- Sem ícone próprio (ícone padrão do Android) e sem resources.arsc.
- O comportamento do WebView (IndexedDB, desempenho, teclado, gestos) em aparelhos reais não foi medido.

## Achado: o `dist/treinador` do pacote original está quebrado
`dist/treinador/index.html` (gerado por `npm run build`, inclusive o do ZIP original) dá `Unexpected token 'export'` e fica em "Carregando Modo Treinador…": o `tools/build.mjs` não trata `export {A,B}` (reexportação) de um módulo. Por isso a APK embute o código-fonte, não o `dist`. Corrigir o build fica como item novo.

## Reconstruir
`MainActivity.java` → `javac --release 8` contra `android-4.1.1.4.jar` (Maven Central) → versão de classe ajustada para 50 → `dx 1.7` (Maven Central) → `axml.py` (manifesto) → zip com `assets/www/...` → `Sign.java` (apksig 2.3.0, `--add-exports java.base/sun.security.x509=ALL-UNNAMED`). A chave (`fu.p12`) não foi versionada.
