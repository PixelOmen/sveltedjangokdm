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
           <section class="mainSections">
                <div class="infoText-Center">
                    <h1>About KDM-GEN</h1>
                    <p>
                        Welcome to KDM-GEN, a fictional web application built with
                        the Django framework. This site is not a real product, but rather a demonstration
                        of a full web stack.
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
                    <h2>Technologies</h2>
                    <ul class="techlist">
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
                            Docker - A platform for developing, shipping, and running applications in containers

                        </li>
                        <li>
                            <img src={checkmark} alt="Checkmark" width="30" class="checkmark">
                            DigitalOcean - A cloud infrastructure provider offering scalable resources
                        </li>
                    </ul>    
                    <br><br><br>
    
                    <h1>Connect With Me</h1>
                    <ul>
                        <li>
                            <img class="linkedin-img" src={emailIcon} alt="email-Icon" width="30px">
                            <NavAnchor data={email_link} newTab={false}/>
                        </li>
                        <li>
                            <img class="linkedin-img" src={githubIcon} alt="github-Icon" width="30px">
                            <NavAnchor data={github_link} newTab={true}/>
                        </li>
                        <li>
                            <img class="linkedin-img" src={linkedinIcon} alt="LinkedIn-Icon" width="30px">
                            <NavAnchor data={linkin_link} newTab={true}/>
                        </li>
                    </ul>
                    <h2 style="margin-top: 30px">Source Code</h2>
                    <img class="linkedin-img" src={githubIcon} alt="LinkedIn-Icon" width="30px">
                    <span style="font-size: 18pt;">
                        <NavAnchor data={sourcecode_link} newTab={true}/>
                    </span>
                </div>
            </section>
        </div>
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
    
    .heroContainer {
        margin-left: auto;
        margin-right: auto;
        max-width: 1300px;
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
        text-align: center;
    }

    p {
        font-size: 18pt;
        margin-top: 0px;
    }

    li {
        font-size: 18pt;
    }

    .techlist {
        /* border: 1px solid red; */
        text-align: left;
        padding-left: 100px;
        /* max-width: 300px; */
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

    h2 {
        margin-bottom: 10px;
        margin-top: 60px;
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
  