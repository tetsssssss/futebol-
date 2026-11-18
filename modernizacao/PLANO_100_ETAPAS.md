# Football Universe v0.15 — plano de 100 etapas (GLB fora do escopo)

Estado: **plano**, não executor automático. Nada abaixo roda sozinho; cada etapa só vale com evidência (captura, medição, teste ou diff). Regras fixas: preservar motor, resultados, saves e fallback 2D; mudanças pequenas e reversíveis (patch + original `.orig`); relatar o que foi só simulado em navegador headless versus aparelho real.
Legenda de status herdada de `PROGRESSO.md`: ✔ feita · ◐ parcial · ✘ pendente · 🆕 nova (ideia minha, separada do pedido original; pode cortar).

## A. Base e segurança (1–10)
1 ✔ Inventário · 2 ✔ Suíte de 167 testes · 3 ◐ Fluxo desktop · 4 ◐ Partida em celular · 5 ✔ Exportar/importar save (hash idêntico) · 6 ◐ Controle de versão (commits + patches) · 7 ✘ Mapa de eventos de partida × estados visuais · 8 ◐ Falha de CDN/WebGL → 2D · 9 ✘ Métricas e aparelhos de referência (definir 2 Androids + 1 iPhone reais, ou declarar que não há) · 10 ✘ Matriz de riscos priorizada.

## B. Campo 2D (11–20)
11 ◐ Enquadramento · 12 ◐ Contraste das linhas · 13 ◐ Bola (falta movimento rápido) · 14 ◐ Equipes/goleiros (falta teste com pares de uniformes reais dos 40 clubes) · 15 ✘ Tamanho dos jogadores · 16 ◐ Posse · 17 ◐ Direção da jogada · 18 ◐ Nomes (desktop ainda sobrepõe em aglomerados) · 19 ◐ Escanteio/lateral/gol sem cortes · 20 ◐ Regressão 2D completa.

## C. Transmissão e interface (21–30)
21 ✘ Hierarquia placar/tempo/equipes · 22 ◐ Feed de eventos · 23 ✘ Câmera transmissão · 24 ✘ Câmera tática · 25 ✘ Câmera da bola · 26 ✔ Velocidade/pausa medidas · 27 ✘ Substituições na tela · 28 ◐ Gols e cartões (precisa partida com gols) · 29 ◐ Replay (mais cenários: gol, cartão, intervalo) · 30 ◐ Modos liga/copa/eliminatórias.

## D. Mobile e acessibilidade (31–40)
31–34 ◐ HUD em 360/390/412/430 (revisão item a item) · 35 ✔ Alvos de toque · 36 ◐ Paisagem (retorno da partida) · 37 ◐ Contraste/tamanho de texto (9–11 px ainda pequeno) · 38 ◐ Teclado · 39 ✘ Menos poluição visual em tela pequena · 40 ◐ Revalidar saves.

## E. Fidelidade do jogo e regras (41–50) — novo bloco, no lugar do 3D
41 ✘ Auditar `rules.js`/`discipline.js` contra as Regras do Jogo (faltas, cartões, acréscimos, pênaltis, prorrogação) · 42 ✘ Simular ≥1.000 partidas e comparar médias com o Brasileirão real (gols/jogo, chutes, faltas, cartões, escanteios) usando dados pesquisados e citados, sem inventar números · 43 ✘ Verificar impedimento: existe? se não, decidir se entra · 44 ✘ Distribuição de resultados (0–0, goleadas, mando de campo) · 45 ✘ Efeito real de formação/mentalidade/pressão no resultado (teste A/B com mesma semente) · 46 ✘ Cansaço e substituições: realismo e impacto · 47 ✘ Lesões (existem? frequência plausível) · 48 ✘ Determinismo: mesma semente → mesmo jogo (garantia + teste) · 49 ✘ Pênaltis e disputa: teste estatístico · 50 ✘ Relatório de plausibilidade esportiva.

## F. Equilíbrio, calendário e carreira (51–60)
51 ✘ Simular 100 temporadas completas: distribuição de campeões/rebaixados · 52 ✘ Força dos 20 clubes sem elenco verificado (aviso "hipotética" já existe): impacto no equilíbrio · 53 ✘ Acesso e descenso A/B conferidos · 54 ✘ Calendário gerado × datas reais (limitação já avisada) · 55 ✘ Libertadores/Sul-Americana: classificação e sorteios · 56 ✘ Evolução de jogadores entre temporadas (idade, potencial) · 57 ✘ Contratos/transferências: o que existe e o que falta · 58 🆕 Modo carreira de treinador (demissão, metas da diretoria, reputação) · 59 🆕 Coletiva de imprensa/moral do elenco, simples e opcional · 60 ✘ Relatório de equilíbrio.

## G. Experiência do treinador (61–70)
61 ✘ Fluxo de escalação (XI, banco) em celular · 62 ✘ Predefinições táticas com explicação do efeito · 63 🆕 Feedback pós-decisão ("o recuo reduziu chances sofridas em X%") · 64 ✘ Substituir: busca, filtro por posição, cansaço visível · 65 ✘ Tabela, artilharia e estatísticas legíveis em 360 px · 66 ✘ Ficha do jogador e comparação · 67 🆕 Resumo pós-jogo com mapa de chutes e xG simples (derivado dos eventos reais) · 68 🆕 Linha do tempo da partida clicável · 69 ✘ Textos e idioma: revisão pt-BR · 70 ✘ Onboarding curto na primeira partida.

## H. Dados, saves e robustez (71–80)
71 ✘ Versionamento do formato de save + migração testada (v0.14 → v0.15) · 72 ✘ Importar arquivo corrompido/malicioso: erro claro, sem perder o save atual · 73 ✘ IndexedDB indisponível/cheio (modo privado): comportamento e aviso · 74 ✘ Múltiplos slots de save + backup automático · 75 ✘ Tamanho do save (592 KB) e tempo de gravação em dispositivo lento · 76 ✘ Dados de fotos/escudos: licenças e fontes (`PHOTO_SOURCES_2026.md`) revisadas · 77 ✘ Sincronizar base 2026 (`sync-pool`): comportamento sem rede · 78 ✘ Teste de propriedade: salvar→carregar→salvar idempotente em vários estados · 79 ✘ Nada de dados pessoais em exportações · 80 ✘ Relatório de robustez.

## I. Desempenho e qualidade (81–90)
81 ✘ Perfil de frames do canvas 2D (desktop e CPU limitada 4×/6×) · 82 ✘ Custo de pintura de 22 jogadores + rótulos; cache de sprites se preciso · 83 ✘ Tamanho dos bundles (`treinador/index.html` ≈ 755 KB) e tempo de carga em 3G simulado · 84 ✘ Carregamento do Babylon via CDN: versão fixa, SRI, timeout e mensagem de fallback; testar caminho com CDN acessível · 85 🆕 Modo offline/PWA (instalável no celular) · 86 ✘ Bateria: reduzir quadros quando a aba está oculta · 87 ✘ Lint/formatação e checagem de tipos leve (JSDoc) sem refatorar o motor · 88 ✘ CI: rodar `npm run test:all` + checagem de overflow mobile a cada push · 89 ✘ Testes visuais automatizados (capturas de referência em 360/390/1440) · 90 ✘ Acessibilidade automatizada (axe) e revisão manual.

## J. Entrega (91–100)
91 ✘ Regressão completa: simulação, saves, UI, modos · 92 ✘ Testes em aparelho físico (se o usuário fornecer) ou declaração explícita da lacuna · 93 ✘ Changelog e README atualizados (sem prometer o que não foi medido) · 94 ✘ Guia de instalação `INICIAR_*` testado em Linux/Windows · 95 ✘ Pacote final: ZIP único + hash + lista de arquivos · 96 ✘ Registro de decisões (por que cada mudança) · 97 ✘ Lista de limitações conhecidas · 98 ✘ Roteiro de continuidade (próximas 50) · 99 ✘ Revisão final de código das mudanças (`/code-review`) · 100 ✘ Entrega verificável: relatório final com evidência por etapa.

## Como eu proporia executar
- **Ordem recomendada:** terminar B/C/D (já em curso e baratas) → E e F (maior ganho de jogo, e mostram se o simulador é crível) → H (proteger saves) → I → J. G e as 🆕 só se você quiser.
- **Lotes de ~10 etapas por rodada**, cada lote com relatório e ZIP novo; sem alegar processamento em segundo plano.
- **Pontos que precisam de decisão sua:** (a) metas reais para E/F (qual média de gols/jogo aceitar como "plausível"; as fontes eu pesquiso e cito); (b) se as 🆕 entram; (c) se existe aparelho físico para a etapa 92.
- **Críticas ao plano:** os blocos B–D, que já tomaram a sessão inteira, são polimento; o maior risco real é a credibilidade do simulador (E/F) e a segurança dos saves (H), que ainda não olhei. Por isso puxei esses blocos para o lugar do 3D.
