import streamlit.components.v1 as components

def show_feedback_carousel():
    carousel_html = """
    <!-- Load Bootstrap CSS and JS first -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    
    <!-- Custom styles loaded after Bootstrap -->
    <style>
    /* Global rule to force all elements to have a transparent background */
    * {
        background: transparent !important;
        background-color: transparent !important;
        background-image: none !important;
    }

    /* Additional specificity for our carousel and its children */
    body, html,
    .carousel-container,
    .carousel-container *,
    .carousel-wrapper,
    .carousel-wrapper *,
    .carousel,
    .carousel *,
    .carousel-inner,
    .carousel-inner *,
    .carousel-item,
    .carousel-item *,
    .feedback-card,
    .feedback-card * {
        background: transparent !important;
        background-color: transparent !important;
    }
    
    /* Base layout styles */
    .carousel-container {
        display: flex;
        gap: 20px;
        margin: 0 -10px;
    }
    .carousel-wrapper {
        flex: 1;
        padding: 0 10px;
    }
    .carousel {
        margin-bottom: 30px;
    }
    .carousel-item {
        padding: 20px;
    }
    .feedback-card {
        border-radius: 8px;
        padding: 24px;
        margin: 10px;
        text-align: center;
        aspect-ratio: 1;
    }
    .feedback-avatar {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        margin: 0 auto 12px;
    }
    .feedback-stars {
        color: #FFD700;
        font-size: 24px;
        margin: 12px 0;
    }
    .feedback-text {
        font-size: 14px;
        color: #ffffff;
        margin: 12px 0;
        line-height: 1.4;
    }
    .feedback-author {
        font-weight: 600;
        color: #ffffff;
        margin: 4px 0;
    }
    </style>
    
    <div class="carousel-container">
        <!-- First Carousel -->
        <div class="carousel-wrapper">
            <div id="carousel1" class="carousel slide" data-ride="carousel" data-interval="3000">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=1" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"The AI capabilities are remarkable. It's transformed our workflow completely!"</p>
                            <p class="feedback-author">Sarah Johnson</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=2" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Incredible time savings. Our team's productivity has doubled!"</p>
                            <p class="feedback-author">James Wilson</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=3" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"User-friendly interface with powerful features. Almost perfect!"</p>
                            <p class="feedback-author">Lisa Chen</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=4" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"The best solution we've found for our documentation needs."</p>
                            <p class="feedback-author">Mike Thompson</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=5" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Game-changing efficiency. Worth every penny!"</p>
                            <p class="feedback-author">Emma Davis</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    
        <!-- Second Carousel -->
        <div class="carousel-wrapper">
            <div id="carousel2" class="carousel slide" data-ride="carousel" data-interval="3500">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=6" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Integration was seamless. Support team is exceptional!"</p>
                            <p class="feedback-author">David Kim</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=7" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"The AI suggestions are spot-on. Saves hours of work!"</p>
                            <p class="feedback-author">Rachel Green</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=8" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Perfect for our enterprise needs. Highly recommend!"</p>
                            <p class="feedback-author">Tom Martinez</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=9" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Innovative features that actually make sense. Great tool!"</p>
                            <p class="feedback-author">Sophie Turner</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=10" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Customer service is outstanding. Always helpful!"</p>
                            <p class="feedback-author">Alex Wong</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    
        <!-- Third Carousel -->
        <div class="carousel-wrapper">
            <div id="carousel3" class="carousel slide" data-ride="carousel" data-interval="4000">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=11" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"The analytics features are incredible. Data-driven decisions made easy!"</p>
                            <p class="feedback-author">Jennifer Lee</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=12" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Revolutionized our documentation process. Simply amazing!"</p>
                            <p class="feedback-author">Chris Evans</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=13" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"The collaboration features are top-notch. Team loves it!"</p>
                            <p class="feedback-author">Maria Garcia</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=14" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Security features are robust. Perfect for enterprise use!"</p>
                            <p class="feedback-author">Robert Smith</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="feedback-card">
                            <img class="feedback-avatar" src="https://i.pravatar.cc/150?img=15" alt="User avatar">
                            <div class="feedback-stars">★★★★★</div>
                            <p class="feedback-text">"Best investment for our company this year. ROI is fantastic!"</p>
                            <p class="feedback-author">Amanda White</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
    $(document).ready(function(){
        // Initialize carousels with distinct intervals
        $('#carousel1').carousel({ interval: 3000, ride: 'carousel', wrap: true });
        $('#carousel2').carousel({ interval: 3500, ride: 'carousel', wrap: true });
        $('#carousel3').carousel({ interval: 4000, ride: 'carousel', wrap: true });
    });
    </script>
    """
    
    components.html(carousel_html, height=500)