# Football Universe v0.15 — fila de 50 etapas: estado final desta sessão (18/11/2026)

ZIP unificado (Parte 1 + Parte 2, 10.077 arquivos, sem duplicatas): `Football_Universe_v0.15_COMPLETO.zip`, já com as correções e `npm run build` refeito (saída 0). Originais preservados como `*.orig` / `*.step1` em `treinador/`. `npm run test:all`: **167 passam, 0 falham** (reexecutado após cada bloco de mudanças).
Ambiente: Chromium headless (Playwright) neste contêiner — **não são aparelhos reais**. A CDN do Babylon fica bloqueada aqui, então só o caminho 2D foi exercitado.

## Alterações (só apresentação; motor, regras, resultados e saves intactos)
| # | Arquivo | O que mudou |
|---|---|---|
| 001 | style.css | `.shell` `minmax(0,1fr)`: página tinha 624 px de largura em 360–430 px (conteúdo cortado, abas inalcançáveis). Agora largura = viewport. |
| 002 | renderer.js | Bola 3,3–5,5 → 4,4–7 px com aro amarelo. |
| 003 | style.css | `@media(pointer:coarse)`: alvos ≥ 44 px (antes: 28–36 botões/controles abaixo disso). |
| 004 | graphics/animations/renderer.js | Campo cabe no canvas com margem ≥ 18 px em todas as câmeras/larguras testadas (broadcast chegava a 1,08× e cortava a bola na borda); linhas mais claras e grossas; portador da bola com anel amarelo + seta; nomes só do portador/selecionado em canvas < 560 px; cor do goleiro escolhida longe das camisas; legenda "TIME ▶ ataca" que **inverte no 2º tempo** (conferido com o goleiro em campo). |

## Status das 50 etapas
Legenda: ✔ feita e verificada · ◐ parcial (limitação dita) · ✘ não feita/bloqueada.
1 ✔ inventário (2 ZIPs, 10.077 arquivos, entradas `index.html`, `treinador/index.html`, `copa/`; save em IndexedDB) · 2 ✔ 167 testes · 3 ◐ desktop 1440×900, fluxo até a partida, capturas · 4 ◐ celular 360/390/412/430, capturas, sem aparelho real · 5 ✔ export→novo campeonato→import→re-export: arquivo de 591.988 B **idêntico** (hash igual), em 390 px · 6 ◐ checkpoints por commits e patches; o jogo em si fica no ZIP · 7 ✘ · 8 ◐ CDN bloqueada → campo 2D funciona sem erro; caminho com CDN não testado · 9 ✘ métricas/aparelhos reais não definidos · 10 ✘
11 ◐ campo cabe em 320–900 px (cálculo + capturas); zoom>1 nas câmeras de acompanhamento pode cortar por desenho · 12 ◐ contraste da linha ≈2,4:1 → ≈5,8:1 (estimado por cálculo, alfa aproximado) · 13 ◐ bola maior; movimento rápido não avaliado · 14 ◐ função de cor de goleiro testada em Node (camisas amarelas/vermelhas); uniformes quase iguais já eram tratados por `resolveKits` · 15 ✘ tamanho dos jogadores não alterado (mín. 6,4 px; número 8 px) · 16 ◐ anel+seta no portador (`carrierId` do estado) · 17 ◐ legenda de sentido de ataque; seta de jogada já existia · 18 ◐ nomes ocultos em canvas estreito; no desktop ainda há sobreposição em aglomerados (ex.: "Cruz/Cauly") · 19 ◐ borda corrigida; escanteio/lateral/gol não percorridos um a um · 20 ◐ placar, eventos e controles ativos nas capturas; sem teste de regressão visual
21–29 ✘ (hierarquia do placar, eventos, câmeras, controles de velocidade, substituições, gols/cartões, replay: não revisados nem alterados) · 30 ◐ liga, copa e eliminatórias abrem a partida e rodam em 1440 e 390 px sem erro de página; sem leitura de regressões de resultado
31–34 ◐ 360/390/412/430: sem rolagem lateral, partida abre, toque real em aba funciona; não revisei HUD item a item · 35 ✔ medido: 0 controles <44 px em 360/390/844×390 · 36 ◐ paisagem 844×390 sem estouro lateral; retorno da partida não testado · 37 ◐ contrastes calculados de 8 pares de cor: 6,2–11,6:1 (todos ≥ 4,5); texto de 9–11 px continua pequeno · 38 ◐ Tab percorre todos os controles com foco visível e Enter troca de aba; atalhos de jogo não verificados · 39 ◐ nomes ocultos em telas estreitas; sem comparação de acesso a funções · 40 ◐ save re-verificado em 390 px (etapa 5)
41–48 ✘ **bloqueadas: o GLB anexado não está nesta sessão** (só 2 ZIPs + a fila). Informação extra do `player.glb` *interno* ao pacote (não é o anexo): 428 triângulos, 1 skin, 0 animações, 21 KB; `referee.glb` idêntico em estrutura; nenhum dos 8 GLBs internos tem animação. Nada integrado. · 49 ◐ suíte completa de 167 testes + checagens de navegador acima; sem regressão visual automatizada · 50 ◐ este relatório + ZIP; limitações acima

## Não feito / riscos
- Nada foi testado em celular físico, nem em WebGL real, nem com a CDN acessível.
- Tamanho/legibilidade em desktop (nomes sobrepostos em aglomerados) ainda precisa de decisão de design.
- Etapas 21–29, 7, 9, 10 e todo o bloco 3D permanecem pendentes.
