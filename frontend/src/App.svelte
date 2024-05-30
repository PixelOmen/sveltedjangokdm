<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import Home from "./pages/home.svelte";
  import KDM from "./pages/kdm/KDM.svelte"; // linter error

  export let url = "";
</script>

<Router {url}>
  <Route path="/" component={Home}></Route>
  <Route path="/kdm" component={KDM}></Route>
</Router>