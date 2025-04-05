from log_analyzer.config import get_config


def main():
    config_data = get_config()
    print(f"{config_data.file_paths=}")
    print(f"{config_data.report_name=}")


if __name__ == "__main__":
    main()
