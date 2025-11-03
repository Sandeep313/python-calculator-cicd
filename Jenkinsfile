pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }

    environment {
        PROJECT_NAME = 'Python Calculator'
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('📋 Checkout') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "📋 Checking out ${PROJECT_NAME}"
                    echo "Build: #${BUILD_NUMBER}"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    // In real scenario with Git:
                    // checkout scm

                    sh 'ls -la'
                    sh 'python --version'
                }
            }
        }

        stage('🔧 Setup') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "🔧 Installing dependencies"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh '''
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pip list
                    '''

                    echo "✅ Dependencies installed successfully"
                }
            }
        }

        stage('🔍 Code Quality') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "🔍 Running code quality checks"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh '''
                        echo "Running flake8..."
                        flake8 src tests --max-line-length=100 --statistics || true
                    '''

                    echo "✅ Code quality check completed"
                }
            }
        }

        stage('🧪 Unit Tests') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "🧪 Running unit tests"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    def testResult = sh(
                        script: '''
                            pytest tests/ -v \
                                --junitxml=test-results/junit.xml \
                                --html=test-results/report.html \
                                --self-contained-html \
                                --cov=src \
                                --cov-report=html \
                                --cov-report=xml \
                                --cov-report=term
                        ''',
                        returnStatus: true
                    )

                    if (testResult == 0) {
                        echo "✅ All tests passed!"
                    } else {
                        echo "❌ Some tests failed!"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('📊 Test Coverage') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "📊 Analyzing test coverage"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh '''
                        echo "Test Coverage Summary:"
                        coverage report
                    '''

                    echo "✅ Coverage analysis completed"
                }
            }
        }

        stage('📦 Build Package') {
            steps {
                script {
                    def timestamp = sh(
                        script: 'date +%Y%m%d-%H%M%S',
                        returnStdout: true
                    ).trim()

                    def packageName = "calculator-${timestamp}-build${BUILD_NUMBER}.tar.gz"

                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "📦 Creating package"
                    echo "Name: ${packageName}"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh """
                        tar -czf ${packageName} \
                            src/ \
                            requirements.txt \
                            README.md

                        echo "Package created:"
                        ls -lh ${packageName}
                    """

                    echo "✅ Package created successfully"
                }
            }
        }

        stage('📝 Generate Reports') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "📝 Generating build report"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh '''
                        echo "Build Report" > build-report.txt
                        echo "=============" >> build-report.txt
                        echo "" >> build-report.txt
                        echo "Build Number: ${BUILD_NUMBER}" >> build-report.txt
                        echo "Build Date: $(date)" >> build-report.txt
                        echo "Python Version: ${PYTHON_VERSION}" >> build-report.txt
                        echo "" >> build-report.txt
                        echo "Test Results:" >> build-report.txt
                        echo "-------------" >> build-report.txt
                        coverage report >> build-report.txt

                        cat build-report.txt
                    '''

                    echo "✅ Reports generated"
                }
            }
        }
    }

    post {
        always {
            script {
                echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                echo "📋 PIPELINE SUMMARY"
                echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                echo "Project: ${PROJECT_NAME}"
                echo "Job: ${JOB_NAME}"
                echo "Build: #${BUILD_NUMBER}"
                echo "Status: ${currentBuild.result ?: 'SUCCESS'}"
                echo "Duration: ${currentBuild.durationString}"
                echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                // Archive artifacts
                sh 'ls -R test-results/ htmlcov/ || true'
            }
        }

        success {
            echo "🎉 ✅ Pipeline completed successfully!"
        }

        failure {
            echo "💥 ❌ Pipeline failed!"
        }

        unstable {
            echo "⚠️  Pipeline completed with warnings"
        }
    }
}