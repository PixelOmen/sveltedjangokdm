<script lang="ts">
    import { navigate } from "svelte-routing";
    
    import { validateToken } from '../lib/coms';
    
    import home1 from '../assets/Home_1.png'
    import home2 from '../assets/Home_2.png'
    import home3 from '../assets/Home_3.png'
    import HeroSection from "../lib/sections/HeroSection.svelte";
    import ImportantBtn from "../lib/ui/ImportantBtn.svelte";
    import FooterLarge from "../lib/sections/FooterLarge.svelte";

    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;
    let navLinks: any = [];

    async function isAuth() {
        try {
            var res = await validateToken(SERVER_IP);
        } catch (e) {
            return false;
        }
        return res.ok;
    }

    async function setNavlinks() {
        if (await isAuth()) {
            navLinks = [
                {displayName: "Generate", url: `/kdm`},
                {displayName: "About", url: `/about`},
                {displayName: "Logout", url: `/logout`},
            ]
        } else {
            navLinks = [
                {displayName: "Sign Up / Log In", url: `/login`},
                {displayName: "About", url: `/about`},
            ]
        
        }
    };
    setNavlinks();

    function downloadLeaf() {
        window.open(`${SERVER_IP}/api/public_leaf`, '_blank');
    }
</script>
  



<svelte:head>
    <title>KDM-GEN</title>
</svelte:head>

<HeroSection navLinks={navLinks} paddingTop="150px" paddingBottom="0px">
   <section class="mainSections">
        <div class="infoText-Left">
            <h1>Simplify Your KDM Generation</h1>
            <p>Fast, Secure, and Reliable Key Delivery Messages for Your Digital Cinema Packages.</p>
            <ImportantBtn
                on:click={() => navigate('/signup')}
                content="Get Started"
                padding="10px 20px"
                margin="20px 0px"
            />
            <div style="display: inline; margin-left: 10px;">
                <ImportantBtn
                on:click={downloadLeaf}
                content="Download Certificate"
                padding="10px 20px"
                margin="20px 0px"
                />
            </div>
        </div>
        <div class="infoImg">
            <img src={home1} alt="Main Logo" width="500">
        </div>
    </section>
    <hr>
    <section class="mainSections">
        <div class="infoImg">
            <img src={home2} alt="Main Logo" width="500">
        </div>
        <div class="infoText-Right">
                <h2>Ease of Use</h2>
                <p>Generate KDMs in just a few clicks.</p>
                <h2>Security</h2>
                <p>Top-notch encryption to protect your content.</p>
                <h2>Speed</h2>
                <p>Instant KDM generation and delivery.</p>
                <h2>Support</h2>
                <p>24/7 customer support.</p>
        </div>
    </section>
    <hr>
    <section class="mainSections lastSection">
        <div class="infoText-Left">
            <h1>How It Works</h1>
            <h3>Download Public Certificate</h3>
            <p>Create a DKDM for your DCP CPL</p>
            <h3>Upload DKDM and Device Certificates</h3>
            <p>
                CPL DKDMs and device certificates
                are safely stored for future use.
            </p>
            <h3>Generate KDM</h3>
            <p>Click 'Generate' and get your KDM instantly.</p>
            <h3>Download & Distribute</h3>
            <p>Download the KDM and distribute it as needed.</p>
        </div>
        <div class="infoImg">
            <img src={home3} alt="Main Logo" width="550">
        </div>
    </section>
    <div class="footerContainer">
        <FooterLarge navLinks={navLinks} paddingTop="0px" showBorder={false}/>
    </div>
</HeroSection>



<style>
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

    .lastSection {
        margin-bottom: 100px;
    }

    hr {
        border-color: rgb(86, 127, 139);
        width: 100%;
        margin-bottom: 50px;
        box-sizing: border-box;
    }

    .infoText-Left {
        margin: auto;
        margin-right: 30px;
    }

    .infoText-Right {
        margin: auto;
        margin-left: 150px;
    }
    .infoImg {
        border: 8px solid rgb(86, 127, 139);
        border-radius: 15px;
        height: 100%;
        margin: auto;
    }

    img {
        border-radius: 5px;
        display: block;
    }

    p {
        font-size: 20pt;
        max-width: 700px;
        margin-top: 0px;
    }
    
    h1 {
        margin-top: 0px;
        font-size: 3em;
        margin-bottom: 20px;
    }

    h3 {
        font-size: 1.5em;
        margin-bottom: 10px;
    }

    h2, h3 {
        margin-bottom: 0px;
    }

    .footerContainer {
        background-color: #0f2e36;
        padding-top: 30px;
        padding-bottom: 5px;
    }

</style>
  