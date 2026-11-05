pipeline {
    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    parameters {
        string(
            name: 'EXECUTOR_URL',
            defaultValue: 'http://ggr:4444/wd/hub',
            description: 'Адрес Selenoid'
        )
        string(
            name: 'PRESTASHOP_URL',
            defaultValue: 'http://prestashop',
            description: 'Адрес приложения PrestaShop'
        )
        choice(
            name: 'BROWSER',
            choices: ['firefox', 'chrome'],
            description: 'Браузер'
        )
        string(
            name: 'BROWSER_VERSION',
            defaultValue: '125.0',
            description: 'Версия браузера'
        )
        string(
            name: 'THREADS',
            defaultValue: '2',
            description: 'Количество потоков'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                withEnv([
                    "EXECUTOR_URL=${params.EXECUTOR_URL}",
                    "PRESTASHOP_URL=${params.PRESTASHOP_URL}",
                    "BROWSER=${params.BROWSER}",
                    "BROWSER_VERSION=${params.BROWSER_VERSION}",
                    "THREADS=${params.THREADS}"
                ]) {
                    sh '''
                        rm -rf allure-results

                        .venv/bin/python -m pytest hw8/tests \
                            --executor "$EXECUTOR_URL" \
                            --url "$PRESTASHOP_URL" \
                            --browser "$BROWSER" \
                            --browser-version "$BROWSER_VERSION" \
                            --headless \
                            -n "$THREADS" \
                            --tb=short \
                            --alluredir=allure-results --clean-alluredir
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true

            script {
                if (fileExists('allure-results')) {
                    allure results: [[path: 'allure-results']]
                }
            }
        }
    }
}
