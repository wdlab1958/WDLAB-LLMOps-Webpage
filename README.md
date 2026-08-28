# WDLAB-LLMOps · Landing Page

**Self-Hosted Open Core LLMOps Platform** 소개 웹페이지이자 서비스 이용자 대문(Gateway)입니다.
LLM과 AI 에이전트 서비스를 **관측 · 평가 · 최적화 · 통제 · 증빙**하는 클라우드 SaaS 서비스
**WDLAB-LLMOps v2.0 (Open Core · Phase 21~30 구현 완료, 2026-08)** 을, **2027년 1월 22일 AI 기본법
계도기간 종료**에 대비하는 관점(제34조 고영향 AI 사업자 책무 · ISO 42001/27001 거버넌스 ·
Diagnosis·EE 품질 진단 보고서)에서 소비자가 이해하기 쉬운 언어로 소개합니다.

> 2026-08-28: Phase 21~30(SSO·RBAC·SCIM·멀티테넌시·라이선스·빌링·행위 감사·진단 엔진·AI 기본법 패키지) 구현 완료 반영. 원본 프로젝트 v2.0 기준 내용 동기화. 디자인·구성은 유지하고 본문을 압축,
> AI 전문용어를 줄이고 제34조 ② "결과 도출 기준 설명" 대응을 핵심 메시지로 재구성.

- **Live demo**: https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/
- **Repository**: https://github.com/wdlab1958/WDLAB-LLMOps-Webpage

---

## 핵심 메시지

| 영역 | 요약 |
|---|---|
| 왜 지금 | 2027.01.22 계도기간 종료 → 제34조 위반 시 과태료 3천만원 이하. 금융·증권·물류·판매 AI 서비스가 대상. |
| 제34조 4대 책무 | ① 위험관리 ② **결과 도출 기준 설명(핵심)** ③ 이용자 보호 ④ 책임자 지정·공시 — 운영 중 자동 증빙. |
| ISO 42001 · 27001 | 영향평가·모델 카드·행위 감사를 국제 표준 통제 항목에 매핑, 인증 심사 증거로 재사용. |
| Diagnosis · EE | 5단계 품질 진단 → 4축 스코어카드(품질·안전·준수·성능) → 봉인 기록 연동 보고서(DOCX/PDF). |
| 규제 기관 대응 | 과기정통부 · AISI · NIA · PIPC · MOIS · MCST 사실조사·점검 시 증빙 ZIP 제출. |
| 서비스 방식 | v2.0 Open Core = SaaS. Community(무료·Apache-2.0·자체 설치) / Professional(EE·SMB) / Compliance·Enterprise(EE·중견·대기업) 3 에디션. |
| 대상 사용자 | Community: AI·백엔드 개발자, MLOps·플랫폼 운영자. Professional·Enterprise: PM/PO, 법무·감사·컴플라이언스 담당자 (과금). |
| 경쟁 구도 | 글로벌 LLMOps 9종 · Dataiku(셀프 테스트·Gartner 리더·고가) 모두 SaaS, LRQA는 ISO 42001 공인 인증 발급 기관(보완 파트너) — 한국 AI 기본법 대응은 WDLAB 유일. 근거: `WDLAB_vs_글로벌_LLMOps_9종_비교표.xlsx`, `Dataiku_vs_LRQA_vs_WDLAB-LLMOps_비교표.xlsx`. |
| 멀티 에이전트 | LangGraph · CrewAI · AutoGen 등 47개 프레임워크를 Maestro 5계층 DAG로 표준화. |
| Zero-Cost 추론 | Ollama · vLLM 기반 로컬 모델 운영, 외부 LLM 호출 prefix block. |
| 무결성 봉인 | WORM Append-only + HMAC-SHA256 Merkle 체인. 변조 즉시 탐지. |
| XAI 5계층 | Raw → Feature → Natural Language → Visual → Actionable. `/explain` API. |

## 대문(Gateway) 구성

서비스 이용자가 바로 진입할 수 있는 3개 진입점 + Quick Start를 최상단에 배치했습니다.

- **Workspace UI 접속** — 실행 중인 플랫폼 콘솔 (`localhost:18090`)
- **API 문서 (Swagger)** — FastAPI OpenAPI 문서 (`localhost:18080/docs`)
- **소스 · 매뉴얼** — GitHub 저장소, 사용자 매뉴얼, 릴리스 노트
- **Quick Start** — 인프라 기동 → 플랫폼 기동 → SDK 설치 3단계 (5분)

## 5대 축 (Pillars)

1. **Observability** — Maestro DAG 5-Layer · Gantt · End-to-End Flow · WebSocket Stream
2. **Evaluation** — 19 Metrics (Heuristic 9 / LLM-Judge 7 / Korean 3) · A/B Diff · t-test 유의성
3. **Optimization** — GEPA · MetaPrompt · HRPO · Pareto Frontier
4. **Guardrails** — 한국어 가드레일 8종 · KoreanPII 9패턴 · Injection 15패턴 · Vision PII
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

## v1.4.x 운영 강화 (2026.07)

- **전 화면 도움말 챗봇** — 100% 로컬 LLM 어시스턴트, IME 가드
- **Span Watchdog** — span 유형별 latency budget 계약 + Alerts 발화
- **결정성 경계 라벨링** — determinism 플래그 자동 주입, 첫 확률적 span 요약 API
- **Replay 캡슐 완결성** — seed 관통 · temperature/seed 좌표 기록 · 완결성 점수
- **무손실 수집 (G1'·G2')** — Redis degrade 수집 지속 + ClickHouse 디스크 spill 버퍼
- **스키마 마이그레이션 정식화** — PG Alembic V014~V023 · CH V004~V006

## v2.0 Open Core · Enterprise (Phase 21~30, Unreleased)

코어는 Apache-2.0으로 유지(v1.4.x 영구 동결), 엔터프라이즈 기능은 `ee/` 동적 로딩.
EE 활성 시 223 API paths / 비활성 시 Community degrade.

- **Open Core 라이선스 경계** — ee_loader 동적 결합, CI 경계 검사
- **Enterprise SSO** — OIDC + SAML 2.0, 폐쇄망 Keycloak·AD FS 대응
- **RBAC 5×12×4 + SCIM 2.0** — Okta·Entra ID 프로비저닝
- **Platform Audit** — 사용자 행위 감사, append-only + 일 단위 머클 앵커
- **멀티테넌시** — Org→Workspace→Project 3계층 + PostgreSQL RLS
- **K8s HA** — Helm 차트(HPA·CH 3-replica·Patroni·Sentinel) + k6 부하 하네스
- **엔타이틀먼트·빌링** — Ed25519 오프라인 라이선스 키, phone-home 없음
- **AI 서비스 품질 진단 엔진** — 5단계 상태 머신 · 4축 스코어카드 · 감사 보고서
- **AI 기본법 계도기간 대응** — 고영향 판별 위저드 · 증빙 ZIP · 2027.1 카운트다운
- **셀프서브 온보딩 · SaaS 운영** — signup→trial 14일, RPO 1h · RTO 4h

## 에디션 · 요금제 (초안 — 2027년 초 확정 예정)

| 티어 | 가격 | 범위 |
|---|---|---|
| Community | 무료 (Apache-2.0) | 트레이싱 · 평가 19종 · A/B 유의성 · SDK 3종 · IDE 2종 |
| Professional | 연 1,200만원 / 워크스페이스 | + 가드레일 8종 · 온톨로지 검증 · RBAC · SSO · 진단 엔진 |
| Compliance · Enterprise | 연 3,600만원~ / 법인 | + WORM·머클 · AI 기본법 9개 조항 · SCIM · RTBF · 규제 자문 |

원칙: 좌석 과금 없음 · 폐쇄망/로컬 LLM 무료 유지 · v1.4.x Apache-2.0 영구 동결.

---

## 프로젝트 구조

```
WDLAB-LLMOps_Webpage/
├── index.html        # 단일 페이지 진입점 (사이드바 + Gateway + 17개 섹션)
├── css/
│   └── style.css     # 뉴모피즘 디자인 시스템 (+ Gateway · Pricing · 모바일 메뉴)
├── js/
│   └── app.js        # 스크롤 인터랙션 · 사이드바 활성 상태 · 모바일 햄버거 메뉴
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
