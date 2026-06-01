# WDLAB-LLMOps · Landing Page

**Self-Hosted LLMOps Platform** 소개 웹페이지입니다. LLM과 AI Agent 응용 시스템의
관측 · 평가 · 최적화 · 가드레일 · 투명성을 하나의 계층으로 통합한
자체 호스팅형 플랫폼 **WDLAB-LLMOps v1.4 (Phase 13~24 통합)** 의 아이덴티티 · 핵심 기능 · 아키텍처를
정적 사이트로 제공합니다.

- **Live demo**: https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/
- **Repository**: https://github.com/wdlab1958/WDLAB-LLMOps-Webpage

---

## 핵심 메시지

| 영역 | 요약 |
|---|---|
| 데이터 주권 | 모든 트레이스 · 평가 · 감사 로그 온프레미스 저장. 외부 SaaS 전송 0건. |
| AI 기본법 준수 | 제31조(고지 · 공개) · 제34조(영향평가 · 결정근거 · 이의제기) 자동 증거 누적. |
| 멀티 에이전트 | LangGraph · CrewAI · AutoGen 등 39개 프레임워크를 Maestro 5계층 DAG로 표준화. |
| Zero-Cost 추론 | Ollama · vLLM 기반 로컬 모델 운영, 외부 LLM 호출 prefix block. |
| 무결성 봉인 | WORM Append-only + HMAC-SHA256 Merkle 체인. 변조 즉시 탐지. |
| XAI 5계층 | Raw → Feature → Natural Language → Visual → Actionable. `/explain` API. |

## 5대 축 (Pillars)

1. **Observability** — Maestro DAG 5-Layer · Gantt · WebSocket Stream
2. **Evaluation** — 18 Metrics (Heuristic 9 / LLM-Judge 7 / Korean 2) · A/B Diff
3. **Optimization** — GEPA · MetaPrompt · HRPO · Pareto Frontier
4. **Guardrails** — Korean PII 9종 · Prompt Injection 15패턴 · 키 유출 탐지
5. **Transparency** — AI 기본법 §31·§34 · WORM Ledger · Decision Basis · Monthly Report

## Phase 13~24 신규 역량 (v1.4)

이전 "Future" 로드맵 7개 항목을 모두 구현·통합했습니다.

1. **End-to-End Replay** — 트레이스 읽기전용 재실행 + 토큰·지연·출력 Δ Diff
2. **통계적 A/B 유의성** — Paired t-test · p-value · 95% CI (scipy 없이 `math.erfc`)
3. **Vision Guardrails** — 이미지 OCR(PaddleOCR→pytesseract→easyocr 폴백) → 한국어 PII
4. **Distributed Maestro** — Redis Streams 분산 디스패치 · 용량 가중 RR · 60s 하트비트
5. **TS/Java SDK** — `@wdlab/llmops`(Node18+) · `ai.wdlab:llmops`(JDK11+), 의존성 0
6. **IDE Plugins** — VS Code · JetBrains/IntelliJ, 커서 UUID → Trace Detail 점프
7. **RTBF 워크플로** — 잊힐 권리 삭제(개인정보보호법 §36 · GDPR 17), 해시 보존 마스킹

---

## 프로젝트 구조

```
WDLAB-LLMOps_Webpage/
├── index.html        # 단일 페이지 진입점 (사이드바 + 13개 섹션)
├── css/
│   └── style.css     # 뉴모피즘 디자인 시스템
├── js/
│   └── app.js        # 스크롤 인터랙션 · 사이드바 활성 상태
└── assets/           # 이미지 · 다이어그램 (옵션)
```

순수 HTML/CSS/JS로 작성되어 빌드 단계가 없습니다.

## 로컬 미리보기

```bash
# 1. 저장소 클론
git clone https://github.com/wdlab1958/WDLAB-LLMOps-Webpage.git
cd WDLAB-LLMOps-Webpage

# 2. 정적 서버 기동 (Python 3 기준)
python3 -m http.server 8080 --bind 0.0.0.0

# 3. 브라우저에서 접속
#   - 로컬 머신:    http://localhost:8080/
#   - 같은 LAN:     http://<서버 IP>:8080/
```

Node.js 환경이라면 `npx serve .` 로도 동일하게 구동됩니다.

## 배포

`main` 브랜치 루트(`/`)를 소스로 사용하는 **GitHub Pages**로 자동 배포됩니다.
`main` 으로 푸시하면 Pages 빌드가 트리거되어 수 분 내 라이브 URL에 반영됩니다.

```bash
git add <변경 파일>
git commit -m "<요약>"
git push origin main
```

배포 상태 확인:

```bash
gh api repos/wdlab1958/WDLAB-LLMOps-Webpage/pages/builds/latest \
  --jq '{status, error: .error.message, updated_at}'
```

## 기여

이슈 · 풀 리퀘스트는 본 저장소의 [Issues](https://github.com/wdlab1958/WDLAB-LLMOps-Webpage/issues) 탭에서
받습니다. 콘텐츠 변경(통계 · 핵심 기능 · 카피)과 디자인 토큰(색상 · 그림자 · 타이포)은
각각 `index.html`, `css/style.css` 한 곳에 집중되어 있어 빠르게 수정할 수 있습니다.
