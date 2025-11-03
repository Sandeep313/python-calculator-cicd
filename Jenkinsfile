pipeline {
    agent any  // ← Changed from docker to any

    environment {
        PROJECT_NAME = 'Python Calculator'
        EMAIL_RECIPIENTS = 'sandeep.arora313@gmail.com'
    }

    stages {
        stage('📋 Checkout') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "📋 Checking out ${PROJECT_NAME}"
                    echo "Build: #${BUILD_NUMBER}"
                    echo "Branch: ${env.GIT_BRANCH}"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh 'ls -la'
                    sh 'python3 --version || echo "Python check"'
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
                        python3 -m pip install --upgrade pip
                        python3 -m pip install -r requirements.txt
                        python3 -m pip list
                    '''

                    echo "✅ Dependencies installed"
                }
            }
        }

        stage('🔍 Code Quality') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "🔍 Running flake8 linting"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    def lintResult = sh(
                        script: 'python3 -m flake8 src tests --max-line-length=100 --statistics',
                        returnStatus: true
                    )

                    if (lintResult == 0) {
                        echo "✅ Code quality check passed"
                    } else {
                        echo "⚠️  Linting found issues"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('🔒 Security Scan') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "🔒 Running Bandit security scan"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    def securityResult = sh(
                        script: '''
                            python3 -m bandit -r src/ -f json -o security-report.json || true
                            python3 -m bandit -r src/ -f txt
                        ''',
                        returnStatus: true
                    )

                    if (securityResult == 0) {
                        echo "✅ No security issues found"
                    } else {
                        echo "⚠️  Security scan found potential issues"
                        echo "Check security-report.json for details"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('🧪 Unit Tests') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "🧪 Running unit tests with coverage"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    def testResult = sh(
                        script: '''
                            python3 -m pytest tests/ -v \
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
                        echo "❌ Tests failed!"
                        currentBuild.result = 'FAILURE'
                        error("Test execution failed")
                    }
                }
            }
        }

        stage('📊 Coverage Report') {
            steps {
                script {
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "📊 Test Coverage Summary"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh 'python3 -m coverage report'

                    echo "✅ Coverage analysis complete"
                }
            }
        }

        stage('📦 Build Artifact') {
            steps {
                script {
                    def timestamp = sh(
                        script: 'date +%Y%m%d-%H%M%S',
                        returnStdout: true
                    ).trim()

                    def artifactName = "calculator-${timestamp}-build${BUILD_NUMBER}.tar.gz"

                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                    echo "📦 Creating artifact: ${artifactName}"
                    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                    sh """
                        tar -czf ${artifactName} src/ requirements.txt README.md
                        ls -lh ${artifactName}
                    """

                    echo "✅ Artifact created"
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
                echo "Project: ${env.PROJECT_NAME}"
                echo "Build: #${BUILD_NUMBER}"
                echo "Status: ${currentBuild.result ?: 'SUCCESS'}"
                echo "Duration: ${currentBuild.durationString}"
                echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            }
        }

        success {
            script {
                echo "🎉 ✅ Pipeline succeeded!"

                emailext (
                    subject: "✅ Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        <h2 style="color: green;">✅ Build Successful!</h2>

                        <h3>Build Information:</h3>
                        <ul>
                            <li><b>Project:</b> ${env.PROJECT_NAME}</li>
                            <li><b>Job:</b> ${env.JOB_NAME}</li>
                            <li><b>Build Number:</b> #${env.BUILD_NUMBER}</li>
                            <li><b>Duration:</b> ${currentBuild.durationString}</li>
                            <li><b>Branch:</b> ${env.GIT_BRANCH}</li>
                        </ul>

                        <h3>Results:</h3>
                        <ul>
                            <li>✅ Code Quality: Passed</li>
                            <li>✅ Security Scan: Passed</li>
                            <li>✅ Unit Tests: Passed</li>
                            <li>✅ Coverage: Complete</li>
                        </ul>

                        <p><a href="${env.BUILD_URL}">View Build Details</a></p>
                        <p><a href="${env.BUILD_URL}console">View Console Output</a></p>
                    """,
                    to: "${env.EMAIL_RECIPIENTS}",
                    mimeType: 'text/html'
                )
            }
        }

        failure {
            script {
                echo "💥 ❌ Pipeline failed!"

                emailext (
                    subject: "❌ Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        <h2 style="color: red;">❌ Build Failed!</h2>

                        <h3>Build Information:</h3>
                        <ul>
                            <li><b>Project:</b> ${env.PROJECT_NAME}</li>
                            <li><b>Job:</b> ${env.JOB_NAME}</li>
                            <li><b>Build Number:</b> #${env.BUILD_NUMBER}</li>
                            <li><b>Duration:</b> ${currentBuild.durationString}</li>
                            <li><b>Branch:</b> ${env.GIT_BRANCH}</li>
                        </ul>

                        <h3>Action Required:</h3>
                        <p>Please check the console output for detailed error information.</p>

                        <p><a href="${env.BUILD_URL}">View Build Details</a></p>
                        <p><a href="${env.BUILD_URL}console">View Console Output</a></p>
                    """,
                    to: "${env.EMAIL_RECIPIENTS}",
                    mimeType: 'text/html'
                )
            }
        }

        unstable {
            script {
                echo "⚠️  Pipeline completed with warnings"

                emailext (
                    subject: "⚠️  Build UNSTABLE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        <h2 style="color: orange;">⚠️  Build Unstable</h2>

                        <h3>Build Information:</h3>
                        <ul>
                            <li><b>Project:</b> ${env.PROJECT_NAME}</li>
                            <li><b>Job:</b> ${env.JOB_NAME}</li>
                            <li><b>Build Number:</b> #${env.BUILD_NUMBER}</li>
                            <li><b>Duration:</b> ${currentBuild.durationString}</li>
                        </ul>

                        <h3>Warnings:</h3>
                        <p>Build completed but some checks reported issues. Please review.</p>

                        <p><a href="${env.BUILD_URL}">View Build Details</a></p>
                    """,
                    to: "${env.EMAIL_RECIPIENTS}",
                    mimeType: 'text/html'
                )
            }
        }
    }
}