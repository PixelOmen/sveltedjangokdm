<script context='module' lang='ts'>
  import type { NavLinks } from '../nav/NavBar.svelte'    
</script>


<script lang="ts">
    import NavBar from '../nav/NavBar.svelte'

    export let navLinks: NavLinks;
    export let paddingTop = "60px";
    export let paddingBottom = "30px";
</script>

<main>
    <NavBar navLinks={navLinks}/>
    <section class="container" style="
      padding-top: {paddingTop};
      padding-bottom: {paddingBottom};
    ">
      <slot></slot>
    </section>
</main>
  
<style>
  main {
    background: radial-gradient(ellipse at 80% -50%, #0f2e36 0%, #0e1d30 30%, transparent 100%),
                radial-gradient(ellipse at 10% 50%, #0f2e36 0%, #0a1c21 40%);
    padding-top: 30px;
  }
  section {
    margin-left: auto;
    margin-right: auto;
  }
</style>
  