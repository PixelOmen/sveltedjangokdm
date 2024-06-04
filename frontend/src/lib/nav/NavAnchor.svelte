<script context="module", lang="ts">
    export interface AnchorData {
        displayName: string;
        url: string;
    }
</script>

<script lang='ts'>
    export let data: AnchorData;
    export let newTab = false;

    $: atarget = newTab ? "_blank" : "_self";
</script>


<a href={data.url} target={atarget} class="link">
    {data.displayName}
</a>


<style>
    a {
        position: relative;
        text-decoration: none;
        font-weight: 500;
        color: rgb(225, 225, 225);
    }
    a:hover {
        color: #7acfde;
    }

    .link::after {
        content: '';
        position: absolute;
        left: 50%;
        bottom: -5px;
        background-color: #7acfde;
        height: 1px;
        width: 0;
        transition: width 0.2s ease-in-out;
        transform: translate(-50%);
    }

    .link:hover::after {
        width: 100%;
    }
</style>