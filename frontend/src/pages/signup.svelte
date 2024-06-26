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

    const loginLink = {
        displayName: "Already have an account?", url: "/login"
    };

    let formElem: HTMLFormElement;
    let flashInvalid: HTMLDivElement;
    let flashPassMatch: HTMLDivElement;
    let flashUserExists: HTMLDivElement;

    $: {
        if (formElem) {
            formElem.addEventListener('submit', (e) => {
                e.preventDefault();
                login();
            })
        }
    }

    function validate() {
        let password = formElem.password.value;
        let password2 = formElem.password2.value;
        if (password !== password2) {
            flashPassMatch.classList.remove('hidden');
            return false;
        }
        return true;
    }

    async function login() {
        flashInvalid.classList.add('hidden');
        flashPassMatch.classList.add('hidden');
        flashUserExists.classList.add('hidden');

        if (!validate()) {
            return;
        }

        let formdata = new FormData(formElem);

        const res = await fetch(`${SERVER_IP}/api/signup`, {
            method: 'POST',
            body: formdata
        })
        if (res.ok) {
            const data = await res.json();
            save_token(data.token);
            navigate('/kdm');
        } else {
            let err = await res.json();
            if (err.detail.toLowerCase().includes('username already exists')) {
                flashUserExists.classList.remove('hidden');
            } else {
                flashInvalid.classList.remove('hidden');
            }
        }
    }
</script>

<svelte:head>
    <title>Signup</title>
</svelte:head>

<main>
    <HeroSection {navLinks}>
        <div class="header">
            <h1>
                Create an account
            </h1>
        </div>
        <form bind:this={formElem} class="container">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required placeholder="Email">            
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required placeholder="Username">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required placeholder="Password">
            <label for="password2">Confirm Password</label>
            <input type="password" id="password2" name="password2" required placeholder="Confirm Password">
            <ImportantBtn
                content="Sign Up"
                padding="10px 20px"
                margin="20px 0px"
            />
            <div bind:this={flashInvalid} class="flash hidden">Invalid Username/Password</div>
            <div bind:this={flashPassMatch} class="flash hidden">Passwords do not match</div>
            <div bind:this={flashUserExists} class="flash hidden">Username already exists</div>
            <ul class="loginLink">
                <NavAnchor data={loginLink}/>
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
            margin-top: 20px !important;
        }

        .container {
            width: 90% !important;
        }
    }
    .header {
        margin-top: 50px;
        text-align: center;
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
        width: 500px;
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box;
    }

    .flash {
        color: red;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 10px;
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

    .loginLink {
        margin: auto;
        margin-top: 5px;
    }

    .hidden {
        display: none;
    }
</style>