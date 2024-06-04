<script lang="ts">
    import { get } from "svelte/store";
    import { navigate } from "svelte-routing";
    
    import { isAuthenticated } from "../stores/auth";

    import linkedinIcon from "../assets/linkedin_icon.svg";
    import githubIcon from "../assets/github_icon.png";
    
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
</script>
  



<svelte:head>
    <title>KDM-GEN</title>
</svelte:head>

<main>
    <HeroSection navLinks={navLinks} paddingTop="120px" paddingBottom="100px">
       <section class="mainSections">
            <div class="infoText-Center">
                <h1>About KDM-GEN</h1>
                <p>
                    Welcome to my fictional project, a web application built with
                    the Django framework. This site is not a real product, but rather a showcase
                    of my skills and the capabilities of the technologies I've used.
                </p>
                <h2>Purpose and Features</h2>
                <p>
                    This project aims to demonstrate seamless user data management
                    while providing a simple and intuitive user experience. The application
                    allows users to generate and download Key Delivery Messages (KDMs) for
                    digital cinema packages (DCPs). The KDMs are generated based on the
                    user's selection of certificates and DKDMs, which they themselves can
                    upload to the application.
                </p>
                <h2>Technologies Used</h2>
                <ul>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        Python - A versatile and widely-used programming language
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        TypeScript - A statically typed superset of JavaScript, enhancing code quality
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        Svelte - A modern, compiler-based JavaScript framework
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        Django - A powerful Python web framework
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        PostgreSQL - A robust, open-source relational database system
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        EC2 (Elastic Compute Cloud) - Amazon's scalable virtual server infrastructure
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        ECS (Elastic Container Service) - AWS's fully managed Docker container orchestration
                    </li>
                    <li>
                        <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                        Fargate - Serverless compute engine for AWS containers, simplifying infrastructure
                    </li>
                </ul>
                <br><br><br>
                <h1>Contact</h1>
                <p>
                    Find me on the following platforms:
                </p>
                <ul>
                    <li>
                        <img class="linkedin-img" src={githubIcon} alt="LinkedIn-Icon" width="30px">
                        <NavAnchor data={github_link} newTab={true}/>
                    </li>
                    <li>
                        <img class="linkedin-img" src={linkedinIcon} alt="LinkedIn-Icon" width="30px">
                        <!-- <a href="https://www.linkedin.com/in/emmanuelacostapost/" target="_blank">
                            linkedin.com/in/emmanuelacostapost
                        </a> -->
                        <NavAnchor data={linkin_link} newTab={true}/>
                    </li>
            </div>
        </section>
    </HeroSection>
    <div class="footerContainer">
        <FooterLarge navLinks={navLinks} paddingTop="0px" showBorder={false}/>
    </div>
</main>



<style>
    main {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    .mainSections {
        display: flex;
        margin-left: auto;
        margin-right: auto;
        margin-top: 0px;
        margin-bottom: 50px;
        padding: 0px 50px;
        max-width: 1800px;
        align-items: center;
    }

    p {
        font-size: 18pt;
        margin-top: 0px;
    }

    li {
        font-size: 18pt;
    }

    .linkedin-img {
        transform: translateY(7px);
        margin-right: 10px;
    }
    
    h1 {
        font-size: 4em;
        margin-top: 0px;
        margin-bottom: 0px;
    }

    .checkmark {
        transform: translateY(8px);
    }

    .footerContainer {
        margin-top: auto;
        background-color: #0f2e36;
        padding-top: 30px;
        padding-bottom: 5px;
    }

</style>
  