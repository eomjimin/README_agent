### [해당 README.md는 이 프로그램을 실행하여 생성한 파일입니다.]
# 📁 프로젝트 제목: 파일 처리 에이전트 및 도구

## 📖 개요 / 설명
이 프로젝트는 파일 처리, 보기, 작성, 검토 및 검색 기능을 위한 다양한 에이전트와 도구로 구성되어 있습니다. 각 에이전트는 특정 작업을 수행하며, 도구는 README 파일 관리 및 파일 작업을 지원합니다.

## ⚙️ 설치 방법
1. 프로젝트를 클론합니다:
   ```bash
   git clone <repository-url>
   ```
2. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 사용 방법
1. `main.py` 파일을 실행하여 애플리케이션을 시작합니다:
   ```bash
   python main.py
   ```
2. CLI를 통해 다양한 기능을 사용할 수 있습니다.

## ✨ 주요 기능
1. 파일 보기 기능 (`file_viewer_agent.py`)
2. 파일 작성 기능 (`write_agent.py`)
3. 콘텐츠 검토 기능 (`review_agent.py`)
4. 파일 검색 기능 (`search_agent.py`)
5. README 파일 검토 도구 (`review_readme_tool.py`)
6. 웹 검색 도구 (`search_web_tool.py`)
7. README 파일 작성 도구 (`write_readme_tool.py`)

## 🗂️ 폴더 구조
- **agents**: 파일 작업을 위한 에이전트들
  - `file_viewer_agent.py`
  - `write_agent.py`
  - `review_agent.py`
  - `search_agent.py`
- **tools**: 파일 작업 및 README 관리 도구
  - `file_viewer_tools.py`
  - `review_readme_tool.py`
  - `search_web_tool.py`
  - `write_readme_tool.py`
- **기타 파일**:
  - `model.py`: 모델 정의
  - `cli.py`: CLI 기능 처리
  - `main.py`: 애플리케이션의 주요 진입점
  - `requirements.txt`: 프로젝트 의존성 목록

## 🙌 기여 방법
기여를 원하시는 분은 이 저장소를 포크한 후, 변경 사항을 커밋하고 풀 리퀘스트를 제출해 주세요.

## 📄 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다.
