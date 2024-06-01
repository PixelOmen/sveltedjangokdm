<script lang="ts">
    import HeroSection from "../lib/sections/HeroSection.svelte";

    const navLinks = [
        {displayName: "Generate", url: `/kdm`},
        {displayName: "Contact", url: `/contact`},
        {displayName: "About", url: `/about`},
    ]
</script>
  
<svelte:head>
    <title>KDM-GEN</title>
</svelte:head>

<HeroSection navLinks={navLinks}>
   <section id="hero">
        <h1>Simplify Your KDM Generation</h1>
        <p>Fast, Secure, and Reliable Key Delivery Messages for Your Digital Cinema Packages.</p>
        <a href="#get-started" class="cta">Get Started</a>
    </section>
    <section id="features">
        <div class="feature">
            <h2>Ease of Use</h2>
            <p>Generate KDMs in just a few clicks.</p>
        </div>
        <div class="feature">
            <h2>Security</h2>
            <p>Top-notch encryption to protect your content.</p>
        </div>
        <div class="feature">
            <h2>Speed</h2>
            <p>Instant KDM generation and delivery.</p>
        </div>
        <div class="feature">
            <h2>Support</h2>
            <p>24/7 customer support.</p>
        </div>
    </section>
    <section id="how-it-works">
        <h2>How It Works</h2>
        <div class="steps">
            <div class="step">
                <h3>1. Upload DCP</h3>
                <p>Upload your DCP files securely.</p>
            </div>
            <div class="step">
                <h3>2. Enter Details</h3>
                <p>Provide the necessary details for KDM generation.</p>
            </div>
            <div class="step">
                <h3>3. Generate KDM</h3>
                <p>Click 'Generate' and get your KDM instantly.</p>
            </div>
            <div class="step">
                <h3>4. Download & Distribute</h3>
                <p>Download the KDM and distribute it as needed.</p>
            </div>
        </div>
    </section>
    <section id="testimonials">
        <h2>What Our Clients Say</h2>
        <div class="testimonial">
            <p>"This service has revolutionized our workflow!"</p>
            <h3>- Client Name</h3>
        </div>
        <div class="testimonial">
            <p>"Fast and reliable KDM generation every time."</p>
            <h3>- Client Name</h3>
        </div>
    </section>
    <section id="pricing">
        <h2>Pricing Plans</h2>
        <div class="plan">
            <h3>Basic</h3>
            <p>Features and price details.</p>
            <a href="#choose-plan" class="cta">Choose Plan</a>
        </div>
        <div class="plan">
            <h3>Pro</h3>
            <p>Features and price details.</p>
            <a href="#choose-plan" class="cta">Choose Plan</a>
        </div>
        <div class="plan">
            <h3>Enterprise</h3>
            <p>Features and price details.</p>
            <a href="#choose-plan" class="cta">Choose Plan</a>
        </div>
    </section>
    <footer>
        <div class="footer-links">
            <a href="#privacy-policy">Privacy Policy</a>
            <a href="#terms-of-service">Terms of Service</a>
            <a href="#faq">FAQ</a>
        </div>
        <div class="contact-info">
            <p>Email: info@company.com</p>
            <p>Phone: +123 456 7890</p>
            <p>Address: 1234 Street Name, City, Country</p>
        </div>
        <div class="social-media">
            <a href="#facebook">Facebook</a>
            <a href="#twitter">Twitter</a>
            <a href="#linkedin">LinkedIn</a>
        </div>
    </footer>
</HeroSection>

<style>

#hero {
    text-align: center;
    background: url('cinema.jpg') no-repeat center center/cover;
    color: #fff;
    padding: 100px 20px;
}

#hero .cta {
    background-color: #007BFF;
    padding: 15px 30px;
    border-radius: 5px;
    color: #fff;
    text-decoration: none;
}

#features, #how-it-works, #testimonials, #pricing {
    padding: 50px 20px;
    text-align: center;
}

#features .feature, #how-it-works .step, #pricing .plan {
    margin: 20px 0;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

footer .footer-links, .contact-info, .social-media {
    margin: 10px 0;
}

footer .footer-links a, .social-media a {
    color: #fff;
    text-decoration: none;
    margin: 0 10px;
}

</style>
  