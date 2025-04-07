from log_analyzer.config import get_config
from log_analyzer.report_factory import ReportServiceCreator


def main():
    config_data = get_config()
    report_service = ReportServiceCreator.create(config_data.report_name)
    report_service.execute(config_data.file_paths)


if __name__ == "__main__":
    main()
