<script lang="ts">
    import { get } from "svelte/store";
    
    import { isAuthenticated } from "../stores/auth";

    import linkedinIcon from "../assets/linkedin_icon.svg";
    import githubIcon from "../assets/github_icon.png";
    import emailIcon from "../assets/email_icon.svg";
    
    import HeroSection from "../lib/sections/HeroSection.svelte";
    import NavAnchor from "../lib/nav/NavAnchor.svelte";
    import checkmark from '../assets/checkmark.svg'
    import FooterLarge from "../lib/sections/FooterLarge.svelte";

    let navLinks = [{displayName: "Home", url: `/`}];

    if (get(isAuthenticated)) {
        navLinks = navLinks.concat([
            {displayName: "Generate", url: `/kdm`},
            {displayName: "About", url: `/about`},
            {displayName: "Logout", url: `/logout`},
        ]);
    } else {
        navLinks = navLinks.concat([
            {displayName: "Sign Up / Log In", url: `/login`},
            {displayName: "About", url: `/about`},
        ]);
    }

    let github_link = {displayName: "github.com/PixelOmen", url: "https://github.com/PixelOmen"};
    let linkin_link = {displayName: "linkedin.com/in/emmanuelacostapost", url: "https://www.linkedin.com/in/emmanuelacostapost"};
    let email_link = {displayName: "3D.Acosta@gmail.com", url: "mailto:3D.Acosta@gmail.com"};
    let sourcecode_link = {displayName: "github.com/PixelOmen/sveltedjangokdm", url: "https://github.com/PixelOmen/sveltedjangokdm"};
</script>
  



<svelte:head>
    <title>KDM-GEN</title>
</svelte:head>

<main>
    <HeroSection navLinks={navLinks} paddingTop="120px" paddingBottom="80px">
        <div class="heroContainer">
            <div class="infoText">
                <h1>About KDM&#x2011;GEN</h1>
                <p>
                    Welcome to KDM-GEN, a fictional web application built with
                    the Django framework. This site is not a real product, but rather a demonstration
                    of a full web stack.
                </p>
                <h2>Purpose and Features</h2>
                <p>
                    This project aims to demonstrate seamless user data management
                    while providing a simple and intuitive user experience. The application
                    allows users to generate and download fake Key Delivery Messages (KDMs) for
                    Digital Cinema Packages (DCPs). The KDMs are generated based on the
                    user's selection of certificates and DKDMs, which they themselves can
                    upload to the application.
                </p>
                <h2>Implements:</h2>
                <ul class="techlist">
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>Python</b> - Versatile and widely-used programming language
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>TypeScript</b> - Statically typed superset of JavaScript, enhancing code quality
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>Responsive Design</b> - Ensuring the application looks great on all devices
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>Svelte</b> - Modern, compiler-based JavaScript framework
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>Django</b> - Powerful Python web framework
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>Django REST Framework</b> - Powerful and flexible toolkit for building Web APIs in Django
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>PostgreSQL</b> - Robust, open-source relational database system
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>Nginx</b> - High-performance web server and reverse proxy server
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>Docker</b> - Platform for developing, shipping, and running applications in containers
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>WhiteNoise</b> - Middleware for serving static files in Django and other Python web apps           
                        </span>
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        <span>
                            <b>DigitalOcean</b> - Cloud infrastructure provider offering scalable resources
                        </span>
                    </li>
                </ul>    
                <br><br><br>

                <h1 style="transform: translateX(-2px)">Connect</h1>
                <div class="connectContainer">
                    <ul>
                        <li>
                            <img class="linkIcon" src={emailIcon} alt="Email Icon" width="30px">
                            <NavAnchor data={email_link} newTab={false} fontSize="1.1em"/>
                        </li>
                        <li>
                            <img class="linkIcon" src={githubIcon} alt="Github Icon" width="30px">
                            <NavAnchor data={github_link} newTab={true} fontSize="1.1em"/>
                        </li>
                        <li>
                            <img class="linkIcon linkedInIcon" src={linkedinIcon} alt="LinkedIn Icon" width="30px">
                            <NavAnchor data={linkin_link} newTab={true}/>
                        </li>
                    </ul>
                    <h2 style="margin-top: 30px">Source Code</h2>
                    <div class='sourceCode'>
                        <img class="linkIcon" src={githubIcon} alt="Github Icon" width="30px">
                        <NavAnchor data={sourcecode_link} newTab={true}/>
                    </div>
                </div>
            </div>
        </div>
    </HeroSection>
    <div class="footerContainer">
        <FooterLarge navLinks={navLinks} paddingTop="0px" showBorder={false}/>
    </div>
</main>



<style>
    @media (min-width: 1400px) {
        .heroContainer {
            max-width: 1300px !important;
        }
    }

    @media (max-width: 1188px) {
        .techlist > li {
            margin-bottom: 20px !important;
        }
    }

    @media (max-width: 700px) {
        h1 {
            font-size: 2.5em !important;
        }

        h2 {
            font-size: 1.5em !important;
        }
        p {
            font-size: 1.2em !important;
        }

        .techlist > li {
            font-size: 1.2em !important;
        }
    }

    @media (max-width: 500px) {
        .connectContainer {
            font-size: 0.8em !important;
        }
    }

    @media (max-width: 410px) {
        .connectContainer {
            font-size: 0.7em !important;
        }
    }

    main {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
        
    .heroContainer {
        /* border: 1px solid blue; */
        margin-left: auto;
        margin-right: auto;
        max-width: 90%;
        overflow: hidden;
    }

    h1 {
        word-break: keep-all;
        font-size: 4em;
        margin-top: 0px;
        margin-bottom: 0px;
    }

    h2 {
        margin-bottom: 10px;
        margin-top: 60px;
    }
        
    p {
        font-size: 1.5rem;
        margin-top: 0px;
    }
    
    .techlist > li {
        display: flex;
        margin-bottom: 5px;
        font-size: 1.5em;
    }

    .checkmark {
        min-width: 30px !important;
        align-self: flex-start;
        margin-right: 5px;
        transform: translateY(2px) translateX(-5px);
    }

    .connectContainer {
        margin-left: 5px;
    }

    .linkIcon {
        transform: translateY(8px);
        margin-right: 10px;
    }

    .linkedInIcon {
        transform: translateY(9px);
    }
    
    .sourceCode {
        display: flex;
        align-items: center;
    }

    .sourceCode > .linkIcon {
        transform: translateY(0px);
    }

    .footerContainer {
        margin-top: auto;
        background-color: #0f2e36;
        padding-top: 30px;
        padding-bottom: 5px;
    }

</style>
  