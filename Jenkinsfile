pipeline {
    agent any

    options {
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
    }

    parameters {
        string(
            name: 'SELENOID_URL',
            defaultValue: 'http://localhost:4444/wd/hub'
        )
        string(
            name: 'BASE_URL',
            defaultValue: 'http://localhost:8081',
        )
        choice(
            name: 'BROWSER',
            choices: ['firefox', 'chrome']
        )



    }


    stages {
            stage('Checkout') {
                steps {
                    checkout scm
                    sh 'ls -la hw8/tests | head'
                }
            }

            stage('Build test image') {
                steps {
                    sh 'docker build -t hw8-tests:latest .'
                }
            }

            stage('Run tests') {
                steps {
                    sh '''
                        set -e
                        rm -rf allure-results
                        mkdir -p allure-results

                        docker run --rm \
                        --network host \
                        -e SELENOID_URL="$SELENOID_URL" \
                        -e BASE_URL="$BASE_URL" \
                        -v "$WORKSPACE/allure-results:/app/allure-results" \
                        hw8-tests:latest \
                        -v --tb=short \
                        --browser="$BROWSER" \
                        tests/
                    '''
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

                sh 'docker rmi -f hw8-tests:latest || true'
            }
    }
}
