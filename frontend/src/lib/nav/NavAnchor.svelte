<script context="module", lang="ts">
    export interface AnchorData {
        displayName: string;
        url: string;
    }
</script>

<script lang='ts'>
    export let data: AnchorData

    $: atarget = data.displayName.toLowerCase() == "status" ? "_blank" : "_self";
</script>


<li>
    <a href={data.url} target={atarget}>
        {data.displayName}
    </a>
</li>


<style>
    a {
        text-decoration: none;
        color: rgb(225, 225, 225);
    }
    a:hover {
        color: #7acfde;
    }
</style>