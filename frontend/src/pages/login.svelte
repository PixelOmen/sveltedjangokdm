<script lang='ts'>
    import { navigate } from "svelte-routing";

    import { save_token } from "../stores/auth";
    import HeroSection from "../lib/sections/HeroSection.svelte";
    import ImportantBtn from "../lib/ui/ImportantBtn.svelte";
    import NavAnchor from "../lib/nav/NavAnchor.svelte";
    import FooterSmall from "../lib/sections/FooterSmall.svelte";

    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;

    const navLinks = [
        {displayName: "Home", url: `/`},
        {displayName: "About", url: `/about`},
    ]

    const signUpLink = {
        displayName: "Create an account", url: "/signup"
    };

    let formElem: HTMLFormElement;
    let flashElem: HTMLDivElement;

    $: {
        if (formElem) {
            formElem.addEventListener('submit', (e) => {
                e.preventDefault();
                login();
            })
        }
    }

    async function login() {
        flashElem.classList.add('hidden');
        let formdata = new FormData(formElem);

        const res = await fetch(`${SERVER_IP}/api/login`, {
            method: 'POST',
            body: formdata
        })
        if (res.ok) {
            const data = await res.json();
            save_token(data.token);
            navigate('/kdm');
        } else {
            flashElem.classList.remove('hidden');
        }
    }
</script>

<svelte:head>
    <title>Login</title>
</svelte:head>

<main>
    <HeroSection {navLinks}>
        <div class="header">
            <h1>
                Login
            </h1>
        </div>
        <form bind:this={formElem} class="container">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required placeholder="Username">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required placeholder="Password">
            <ImportantBtn
                content="Login"
                padding="10px 20px"
                margin="20px 0px"
            />
            <div bind:this={flashElem} class="flash hidden">Invalid Username/Password</div>
            <ul class="footerUL">
                <NavAnchor data={signUpLink}/>
            </ul>
        </form>
        <FooterSmall {navLinks}
            showBorder={false}
            width="500px"
            paddingTop="50px"
        />
    </HeroSection>
</main>


<style>
    @media (max-width: 1000px) {
        .header {
            margin-top: 50px !important;
        }

        .container {
            width: 90% !important;
        }
    }
    .header {
        margin-top: 50px;
        text-align: center;
        margin-top: 100px;
    }

    h1 {
        margin-bottom: 20px;
    }
    .container {
        border: 1px solid rgb(48, 48, 48);
        background-color: #272727;
        border-radius: 10px;
        padding: 40px 50px;
        padding-bottom: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 450px;
        max-width: 100%;
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box;
    }

    .flash {
        color: red;
        margin-left: auto;
        margin-right: auto;
    }

    label {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    input {
        background-color: rgb(27, 27, 27);
        border: 2px solid rgb(14, 13, 13);
        border-radius: 5px;
        margin-bottom: 20px;
        padding: 10px;
        font-size: 16px;
    }

    input:focus {
        outline: none;
        border: 2px solid #0977e5;
    }

    .hidden {
        display: none;
    }

    .footerUL {
        margin: auto;
        margin-top: 20px;
        margin-bottom: 0px;
    }
</style>