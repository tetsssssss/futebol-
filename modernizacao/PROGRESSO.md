# Football Universe v0.15 — progresso da fila de 50 etapas

ZIP unificado (Parte 1 + Parte 2, sem arquivos duplicados, 10.077 arquivos): `Football_Universe_v0.15_COMPLETO.zip` (já contém a correção 001; `treinador/style.css.orig` guarda o original). Integridade: `unzip -t` OK.

## Etapas verificadas (18/11/2026)
- 1–2 [Concluído] Inventário e suíte: `npm run test:all` → 167 passam, 0 falham (reexecutado no pacote unificado e após a correção).
- 3 [Parcial] Fluxo desktop 1440×900: Novo campeonato → Central → Assistir à partida funciona (captura em `evidencias/d_4_match.png`).
- 4 [Parcial] Celular 360/390/412/430: partida abre; captura 390 px em `evidencias/m390_4_match.png`.
- 8 [Parcial] CDN do Babylon bloqueado neste ambiente (ERR_TUNNEL_CONNECTION_FAILED): o jogo continuou no campo 2D, sem erro de página. Não testado o caminho com CDN acessível.

## Achado real + correção 001 (`001-mobile-overflow.patch`)
Em ≤980 px o `.shell` usava `grid-template-columns:1fr` (= `minmax(auto,1fr)`); o `nav` com `nowrap` forçava a coluna a 591–624 px. Resultado medido: `scrollWidth` 624 contra viewport de 360/390/412/430 → página cortada à direita e abas ("Partida ao vivo") inalcançáveis por clique.
Correção: `minmax(0,1fr)` + `.sidebar{min-width:0}`. Depois: `scrollWidth` = largura da viewport nos 4 tamanhos; 167 testes continuam passando.
Não testado ainda: o nav rola horizontalmente por toque (só medi o layout).

## Pendente
Etapas 5–7, 9–10 e 11–50 não foram executadas. O GLB do atleta não estava entre os anexos desta sessão (só dois ZIPs e a fila); as etapas 41–48 dependem dele — reenvie. O `player.glb` interno do pacote é outro arquivo.

## Atualização — etapa 13 (bola rastreável), parcial
Correção 002 (`002-bola-visivel.patch`, `treinador/renderer.js`, original em `renderer.js.orig`): raio da bola 3,3–5,5 px → 4,4–7 px, com aro amarelo. Só desenho 2D; motor, resultados e saves intactos. 167 testes passam. Capturas: `evidencias/*_ball_after.png`.
Não validado: movimentos rápidos em sequência (só um quadro por tamanho).

## Achados novos (não corrigidos)
- Etapa 18: em 390 px os nomes dos jogadores se sobrepõem a ponto de ficarem ilegíveis (existe o botão `view-names`; falta ocultar/encurtar por padrão em tela estreita).
- Etapa 19: a bola na lateral/canto aparece cortada na borda do canvas (captura `m390_ball_after.png`).
