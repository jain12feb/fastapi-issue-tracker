from fastapi import FastAPI
from app.routes.issues import router as issue_routes
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.timing import timing_middleware
from app.middlewares.log_request_and_response_details import log_request_response
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Issue Tracker API",
    description="A simple API for tracking issues, allowing you to create, read, update, and delete issues. Each issue has a title, description, status, and a unique ID.",
    version="1.0.0",
)

app.middleware("http")(timing_middleware)
app.middleware("http")(log_request_response)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(issue_routes, prefix="/api/v1")    

@app.get("/", response_class=HTMLResponse)
async def root():
    # i want to return html page with a link to the api documentation
    return """    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IssueFlow - Modern Issue Tracking API</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --secondary: #8b5cf6;
            --accent: #ec4899;
            --dark: #0f172a;
            --dark-light: #1e293b;
            --gray: #64748b;
            --light: #f8fafc;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
        }

        body {
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            color: var(--dark);
            overflow-x: hidden;
        }

        /* Navigation */
        nav {
            position: fixed;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            z-index: 1000;
            padding: 1rem 0;
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
            align-items: center;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .btn {
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            # background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.3);
        }

        .btn-outline {
            border: 2px solid var(--primary);
            color: var(--primary);
            background: transparent;
        }

        .btn-outline:hover {
            background: var(--primary);
            color: white;
        }

        /* Hero Section */
        .hero {
            padding: 8rem 2rem 4rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        }

        .hero-content {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            position: relative;
            z-index: 1;
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            color: white;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.25rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 2rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-bottom: 3rem;
        }

        .version-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        /* Features Section */
        .features {
            padding: 5rem 2rem;
            background: var(--light);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            color: var(--dark);
        }

        .section-subtitle {
            text-align: center;
            color: var(--gray);
            font-size: 1.125rem;
            margin-bottom: 3rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: all 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.1);
        }

        .feature-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .feature-card h3 {
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            color: var(--dark);
        }

        .feature-card p {
            color: var(--gray);
            line-height: 1.7;
        }

        /* API Endpoints Section */
        .api-section {
            padding: 5rem 2rem;
            background: white;
        }

        .endpoints-grid {
            display: grid;
            gap: 1.5rem;
            margin-top: 3rem;
        }

        .endpoint-card {
            background: var(--light);
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.3s;
        }

        .endpoint-card:hover {
            border-color: var(--primary);
            box-shadow: 0 8px 16px rgba(99, 102, 241, 0.1);
        }

        .endpoint-header {
            padding: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            background: white;
        }

        .method-badge {
            padding: 0.5rem 1rem;
            border-radius: 6px;
            font-weight: 700;
            font-size: 0.875rem;
            min-width: 80px;
            text-align: center;
        }

        .method-get {
            background: #dbeafe;
            color: #1e40af;
        }

        .method-post {
            background: #d1fae5;
            color: #065f46;
        }

        .method-put {
            background: #fef3c7;
            color: #92400e;
        }

        .method-delete {
            background: #fee2e2;
            color: #991b1b;
        }

        .endpoint-path {
            font-family: 'Courier New', monospace;
            font-weight: 600;
            color: var(--dark);
            flex: 1;
        }

        .endpoint-description {
            padding: 0 1.5rem 1.5rem;
            color: var(--gray);
        }

        /* Stats Section */
        .stats {
            padding: 5rem 2rem;
            background: var(--dark);
            color: white;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 3rem;
            margin-top: 3rem;
        }

        .stat-item {
            text-align: center;
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: var(--gray);
            font-size: 1rem;
        }

        /* CTA Section */
        .cta {
            padding: 5rem 2rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            text-align: center;
            color: white;
        }

        .cta h2 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .cta p {
            font-size: 1.25rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }

        .cta .btn {
            background: white;
            color: var(--primary);
            font-size: 1.125rem;
            padding: 1rem 2rem;
        }

        .cta .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        /* Footer */
        footer {
            background: var(--dark-light);
            color: white;
            padding: 3rem 2rem;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 3rem;
        }

        .footer-section h3 {
            margin-bottom: 1rem;
            font-size: 1.125rem;
        }

        .footer-section ul {
            list-style: none;
        }

        .footer-section ul li {
            margin-bottom: 0.5rem;
        }

        .footer-section a {
            color: var(--gray);
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-section a:hover {
            color: var(--primary);
        }

        .footer-bottom {
            max-width: 1200px;
            text-align: center;
            color: var(--gray);
        }

        /* Code Block */
        .code-block {
            background: var(--dark);
            color: #a5f3fc;
            padding: 1.5rem;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 0.875rem;
            margin-top: 2rem;
            overflow-x: auto;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                font-size: 2rem;
            }

            .hero p {
                font-size: 1rem;
            }

            .hero-buttons {
                flex-direction: column;
                align-items: center;
            }

            .section-title {
                font-size: 1.75rem;
            }

            .endpoint-header {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .animate {
            animation: fadeInUp 0.6s ease-out;
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <div class="logo">
                <i class="fas fa-bug"></i>
                IssueFlow
            </div>
            <ul class="nav-links">
                <li><a href="#features">Features</a></li>
                <li><a href="/docs" class="btn btn-primary">Api Docs</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <div class="version-badge">
                <i class="fas fa-code"></i> API Version 1.0.0 | OAS 3.1
            </div>
            <h1 class="animate">Track Issues Like Never Before</h1>
            <p class="animate">A powerful, developer-friendly API for modern issue tracking. Simple, fast, and reliable issue management for teams of all sizes.</p>
            <div class="hero-buttons animate">
                <a href="/docs" class="btn btn-primary">
                    <i class="fas fa-rocket"></i> Explore API
                </a>
                <a href="/openapi.json" class="btn btn-outline" style="background: rgba(255,255,255,0.2); color: white; border-color: white;">
                    <i class="fas fa-download"></i> OpenAPI Spec
                </a>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features">
        <div class="container">
            <h2 class="section-title">Powerful Features</h2>
            <p class="section-subtitle">Everything you need to manage issues efficiently with our RESTful API</p>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-rocket"></i>
                    </div>
                    <h3>Lightning Fast</h3>
                    <p>Optimized for performance with response times under 100ms. Handle thousands of requests per second.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h3>Secure & Reliable</h3>
                    <p>Enterprise-grade security with authentication, rate limiting, and 99.9% uptime SLA.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-code"></i>
                    </div>
                    <h3>Developer Friendly</h3>
                    <p>RESTful design with comprehensive documentation, SDKs, and interactive API explorer.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-filter"></i>
                    </div>
                    <h3>Advanced Filtering</h3>
                    <p>Query issues by status, priority, assignee, and custom fields with powerful search capabilities.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-sync"></i>
                    </div>
                    <h3>Real-time Updates</h3>
                    <p>Webhook support for instant notifications when issues are created, updated, or resolved.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3>Analytics Ready</h3>
                    <p>Built-in metrics and reporting endpoints to track team performance and issue trends.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats">
        <div class="container">
            <h2 class="section-title" style="color: white;">Trusted by Developers Worldwide</h2>
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">10K+</div>
                    <div class="stat-label">Active Developers</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">1M+</div>
                    <div class="stat-label">API Calls Daily</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">99.9%</div>
                    <div class="stat-label">Uptime SLA</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">&lt;100ms</div>
                    <div class="stat-label">Response Time</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-bottom">
            <p>Built by <a style="color: #007bff;" href="https://github.com/jain12feb" target="_blank">Prince Jain</a> with ❤️ for developers.</p>
        </div>
    </footer>

    <script>
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Add animation on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.feature-card, .endpoint-card, .stat-item').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'all 0.6s ease-out';
            observer.observe(el);
        });
    </script>
</body>
</html>"""


# items : list[dict[str, str]] = [
#     {"id": 1, "name": "Item 1", "description": "This is item 1"},
#     {"id": 2, "name": "Item 2", "description": "This is item 2"},
#     {"id": 3, "name": "Item 3", "description": "This is item 3"},
# ]

# @app.get("/items")
# async def read_items():
#     return items

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):                                                                                                                      
#     try:                                                                                                    
#         return next(item for item in items if item["id"] == int(item_id))                                     
#     except KeyError:
#         return {"error": "Item not found"}
#     except StopIteration:
#         return {"error": "Item not found"}
    
# @app.post("/items")
# async def create_item(item: dict[str, str]):
#     item["id"] = len(items) + 1
#     items.append(item)
#     return item

# @app.put("/items/{item_id}")
# async def update_item(item_id: str, item: dict[str, str]):
#     try:
#         existing_item = next(item for item in items if item["id"] == int(item_id))
#         existing_item.update(item)
#         return existing_item
#     except KeyError:
#         return {"error": "Item not found"}
#     except StopIteration:
#         return {"error": "Item not found"}
    
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: str):
#     try:
#         item = next(item for item in items if item["id"] == int(item_id))
#         items.remove(item)
#         return {"message": "Item deleted"}
#     except KeyError:
#         return {"error": "Item not found"}
#     except StopIteration:
#         return {"error": "Item not found"}

