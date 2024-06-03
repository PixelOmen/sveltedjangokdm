<script lang='ts'>
    import { navigate } from "svelte-routing";

    import { save_token } from "../stores/auth";
    import HeroSection from "../lib/sections/HeroSection.svelte";
    import ImportantBtn from "../lib/ui/ImportantBtn.svelte";
    import FooterLinks from "../lib/sections/FooterLinks.svelte";

    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;

    const navLinks = [
        {displayName: "Home", url: `/`},
        {displayName: "About", url: `/about`},
    ]

    let flashElem: HTMLDivElement;

    async function login() {
        flashElem.classList.add('hidden');
        const res = await fetch(`${SERVER_IP}/api/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "username": "eacosta",
                "password": "mypassword2"
            })
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

<!-- <h3>
    This is the login page
</h3>
<div>
    <button on:click={login}>Login</button>
    <button on:click={() => navigate('/')}>Home</button>
</div> -->

<main>
    <HeroSection {navLinks}>
        <form class="container">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
            <ImportantBtn
                on:click={login}
                content="Login"
                padding="10px 20px"
                margin="20px 0px"
            />
            <div bind:this={flashElem} class="flash hidden">Invalid Username/Password</div>
        </form>
        <FooterLinks {navLinks} showBorder={false}/>
    </HeroSection>
</main>


<style>
    .container {
        border: 1px solid rgb(48, 48, 48);
        background-color: #272727;
        border-radius: 10px;
        padding: 60px 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 400px;
        margin-top: 30px;
        margin-left: auto;
        margin-right: auto;
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
</style>