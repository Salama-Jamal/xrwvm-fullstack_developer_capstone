# Sentiment Analyzer Deployment - Visual Guide

## 🎯 Deployment Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    START DEPLOYMENT                              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 1: Navigate to Directory                                   │
│  $ cd server/djangoapp/microservices                            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 2: Build Docker Image                                      │
│  $ docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer│
│                                                                  │
│  ⏱️  Time: ~2-3 minutes                                          │
│  ✅ Success: "Successfully built [image-id]"                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 3: Push to IBM Container Registry                          │
│  $ docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer     │
│                                                                  │
│  ⏱️  Time: ~1-2 minutes                                          │
│  ✅ Success: "latest: digest: sha256:..."                        │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 4: Deploy to Code Engine                                   │
│  $ ibmcloud ce application create --name sentianalyzer \        │
│      --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer \     │
│      --registry-secret icr-secret --port 5000                   │
│                                                                  │
│  ⏱️  Time: ~1-2 minutes                                          │
│  ✅ Success: "Creating application 'sentianalyzer'... OK"        │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 5: Get Application URL                                     │
│  $ ibmcloud ce application get --name sentianalyzer             │
│                                                                  │
│  📋 Copy the URL from output                                     │
│  Example: https://sentianalyzer.xxxxx.codeengine.appdomain.cloud│
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 6: Test Deployment                                         │
│  $ curl [YOUR_URL]/analyze/Fantastic%20services                 │
│                                                                  │
│  ✅ Expected: {"sentiment": "positive"}                          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 7: Take Screenshot                                         │
│  🌐 Open in browser: [YOUR_URL]/analyze/Fantastic%20services    │
│  📸 Screenshot must show:                                        │
│     - Full URL in address bar                                   │
│     - JSON response: {"sentiment": "positive"}                  │
│  💾 Save as: sentiment_analyzer.png or .jpeg                    │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 8: Update .env File                                        │
│  Edit: server/djangoapp/.env                                    │
│  Add: sentiment_analyzer_url=[YOUR_URL]/                       │
│                                                                  │
│  ⚠️  IMPORTANT: Include trailing slash (/)                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Step 9: Verify Integration                                      │
│  $ python3 manage.py shell                                      │
│  >>> from djangoapp.restapis import analyze_review_sentiments  │
│  >>> analyze_review_sentiments("This is amazing")              │
│                                                                  │
│  ✅ Expected: {'sentiment': 'positive'}                          │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ✅ DEPLOYMENT COMPLETE                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🖥️ Terminal Commands Visualization

### Command 1: Navigate
```bash
┌─────────────────────────────────────────────────────────────┐
│ $ cd server/djangoapp/microservices                         │
│ $ pwd                                                       │
│ /Users/Salama/IBM/xrwvm-fullstack_developer_capstone/     │
│ server/djangoapp/microservices                             │
└─────────────────────────────────────────────────────────────┘
```

### Command 2: Docker Build
```bash
┌─────────────────────────────────────────────────────────────┐
│ $ docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer│
│                                                             │
│ [+] Building 45.2s (10/10) FINISHED                        │
│  => [internal] load build definition from Dockerfile       │
│  => [internal] load .dockerignore                          │
│  => [internal] load metadata for docker.io/library/python  │
│  => [1/5] FROM docker.io/library/python:3.9.18-slim       │
│  => [2/5] WORKDIR /python-docker                          │
│  => [3/5] COPY requirements.txt requirements.txt          │
│  => [4/5] RUN pip3 install -r requirements.txt            │
│  => [5/5] COPY . .                                        │
│  => exporting to image                                     │
│  => => writing image sha256:abc123...                     │
│  => => naming to us.icr.io/namespace/senti_analyzer       │
│                                                             │
│ ✅ Successfully built abc123def456                          │
│ ✅ Successfully tagged us.icr.io/namespace/senti_analyzer:latest│
└─────────────────────────────────────────────────────────────┘
```

### Command 3: Docker Push
```bash
┌─────────────────────────────────────────────────────────────┐
│ $ docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer │
│                                                             │
│ The push refers to repository                              │
│ [us.icr.io/namespace/senti_analyzer]                       │
│ abc123: Pushed                                             │
│ def456: Pushed                                             │
│ ghi789: Pushed                                             │
│ latest: digest: sha256:xyz789... size: 1234               │
│                                                             │
│ ✅ Push complete                                            │
└─────────────────────────────────────────────────────────────┘
```

### Command 4: Code Engine Deploy
```bash
┌─────────────────────────────────────────────────────────────┐
│ $ ibmcloud ce application create --name sentianalyzer \    │
│     --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer \ │
│     --registry-secret icr-secret --port 5000               │
│                                                             │
│ Creating application 'sentianalyzer'...                    │
│ Run 'ibmcloud ce application get -n sentianalyzer' to     │
│ see more details.                                          │
│                                                             │
│ ✅ OK                                                       │
└─────────────────────────────────────────────────────────────┘
```

### Command 5: Get URL
```bash
┌─────────────────────────────────────────────────────────────┐
│ $ ibmcloud ce application get --name sentianalyzer         │
│                                                             │
│ Getting application 'sentianalyzer'...                     │
│ OK                                                          │
│                                                             │
│ Name:          sentianalyzer                               │
│ Project Name:  your-project                                │
│ Age:           2m                                          │
│ URL:           https://sentianalyzer.xxxxx.us-south.      │
│                codeengine.appdomain.cloud                  │
│ Status:        Ready                                       │
│                                                             │
│ 📋 Copy this URL ☝️                                         │
└─────────────────────────────────────────────────────────────┘
```

### Command 6: Test
```bash
┌─────────────────────────────────────────────────────────────┐
│ $ curl https://sentianalyzer.xxxxx.codeengine.appdomain.cloud/analyze/Fantastic%20services│
│                                                             │
│ {"sentiment": "positive"}                                  │
│                                                             │
│ ✅ Test passed!                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🌐 Browser View

### What You Should See in Browser

```
┌─────────────────────────────────────────────────────────────────┐
│ 🔒 https://sentianalyzer.xxxxx.codeengine.appdomain.cloud/analyze/Fantastic%20services│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                                                                 │
│   {"sentiment": "positive"}                                    │
│                                                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
     ↑                                    ↑
     |                                    |
  Full URL                          JSON Response
  (must be visible)                 (must show positive)
```

### Screenshot Requirements

✅ **Good Screenshot:**
```
┌─────────────────────────────────────────────────────────────────┐
│ Address Bar: https://sentianalyzer.xxxxx.../analyze/Fantastic%20services│
│                                                                 │
│ Page Content: {"sentiment": "positive"}                        │
└─────────────────────────────────────────────────────────────────┘
```

❌ **Bad Screenshot:**
```
┌─────────────────────────────────────────────────────────────────┐
│ Address Bar: [Not visible or cut off]                          │
│                                                                 │
│ Page Content: {"sentiment": "positive"}                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 .env File Configuration

### Before (Default)
```
┌─────────────────────────────────────────────────────────────┐
│ File: server/djangoapp/.env                                 │
├─────────────────────────────────────────────────────────────┤
│ backend_url=http://localhost:3030                           │
│ sentiment_analyzer_url=http://localhost:5050/               │
└─────────────────────────────────────────────────────────────┘
```

### After (Updated)
```
┌─────────────────────────────────────────────────────────────┐
│ File: server/djangoapp/.env                                 │
├─────────────────────────────────────────────────────────────┤
│ backend_url=http://localhost:3030                           │
│ sentiment_analyzer_url=https://sentianalyzer.xxxxx.        │
│ codeengine.appdomain.cloud/                                 │
│                            ↑                                │
│                    Trailing slash required!                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Diagram

```
┌──────────────┐
│   User       │
│   Request    │
└──────┬───────┘
       │
       │ "Analyze: This is great"
       ▼
┌──────────────────────────────────────┐
│   Django Application                 │
│   (restapis.py)                      │
│                                      │
│   analyze_review_sentiments(text)   │
│   ├─ Constructs URL                 │
│   ├─ Makes GET request              │
│   └─ Returns JSON                   │
└──────┬───────────────────────────────┘
       │
       │ HTTP GET: /analyze/This%20is%20great
       ▼
┌──────────────────────────────────────┐
│   Code Engine Microservice           │
│   (Flask app.py)                     │
│                                      │
│   @app.get('/analyze/<text>')       │
│   ├─ Receives text                  │
│   ├─ NLTK VADER analysis            │
│   ├─ Calculates scores              │
│   └─ Determines sentiment           │
└──────┬───────────────────────────────┘
       │
       │ {"sentiment": "positive"}
       ▼
┌──────────────────────────────────────┐
│   Response to User                   │
│   ✅ Sentiment: Positive             │
└──────────────────────────────────────┘
```

---

## 🎨 Sentiment Analysis Logic

```
Input Text: "Fantastic services"
           ↓
┌─────────────────────────────────────┐
│   NLTK VADER Analyzer               │
│                                     │
│   Calculates Scores:                │
│   ├─ Positive (pos): 0.8           │
│   ├─ Negative (neg): 0.0           │
│   ├─ Neutral (neu):  0.2           │
│   └─ Compound:       0.7            │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│   Classification Logic              │
│                                     │
│   if neg > pos and neg > neu:      │
│       return "negative"             │
│   elif neu > neg and neu > pos:    │
│       return "neutral"              │
│   else:                             │
│       return "positive"  ← Selected │
└─────────────────┬───────────────────┘
                  │
                  ▼
         {"sentiment": "positive"}
```

---

## 📊 Testing Matrix

| Input Text | Expected Sentiment | Test Status |
|------------|-------------------|-------------|
| "Fantastic services" | positive | [ ] |
| "Excellent product" | positive | [ ] |
| "Amazing experience" | positive | [ ] |
| "Terrible service" | negative | [ ] |
| "Horrible experience" | negative | [ ] |
| "Worst ever" | negative | [ ] |
| "It is okay" | neutral | [ ] |
| "Average service" | neutral | [ ] |

---

## 🚦 Status Indicators

### Deployment Status
```
🔴 Not Started    - Haven't begun deployment
🟡 In Progress    - Currently deploying
🟢 Complete       - Successfully deployed
```

### Test Results
```
✅ Passed         - Test successful
❌ Failed         - Test failed
⚠️  Warning       - Test passed with warnings
⏭️  Skipped       - Test not run
```

### Application Health
```
🟢 Healthy        - All systems operational
🟡 Degraded       - Some issues detected
🔴 Down           - Service unavailable
```

---

## 🎯 Quick Decision Tree

```
Need to deploy?
    │
    ├─ Yes → Have IBM Cloud access?
    │         │
    │         ├─ Yes → Use automated script (deploy.sh)
    │         │
    │         └─ No → Get IBM Cloud credentials first
    │
    └─ No → Already deployed?
              │
              ├─ Yes → Need to update?
              │         │
              │         ├─ Yes → Rebuild and redeploy
              │         │
              │         └─ No → You're done! ✅
              │
              └─ No → Start deployment process
```

---

## 📱 Mobile-Friendly Testing

If testing from mobile browser:
```
1. Open browser on phone
2. Navigate to: [YOUR_URL]/analyze/test
3. Should see: {"sentiment": "positive"} or similar
4. Take screenshot if needed
```

---

## 🔧 Troubleshooting Visual Guide

```
Problem: Docker build fails
    ↓
Check: Is Docker running?
    ├─ No → Start Docker Desktop
    └─ Yes → Check Dockerfile syntax
              ↓
         Fix errors and retry

Problem: Push fails
    ↓
Check: Logged into IBM Cloud?
    ├─ No → Run: ibmcloud login
    └─ Yes → Check namespace variable
              ↓
         Verify: echo $SN_ICR_NAMESPACE

Problem: Deployment fails
    ↓
Check: Application already exists?
    ├─ Yes → Delete and redeploy
    └─ No → Check Code Engine quota
              ↓
         Review error message

Problem: URL not working
    ↓
Check: Application status
    ↓
Run: ibmcloud ce application get --name sentianalyzer
    ↓
Status: Ready?
    ├─ No → Wait or check logs
    └─ Yes → Verify URL is correct
```

---

## ✨ Success Indicators

You know deployment is successful when you see:

1. ✅ Docker build completes without errors
2. ✅ Docker push shows "digest: sha256:..."
3. ✅ Code Engine shows "OK"
4. ✅ Application status shows "Ready: true"
5. ✅ curl returns `{"sentiment": "positive"}`
6. ✅ Browser displays JSON correctly
7. ✅ Django integration works
8. ✅ No errors in logs

---

**Ready to deploy? Follow the flow chart from top to bottom!** 🚀
