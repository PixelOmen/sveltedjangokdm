<script lang="ts">
  import { Router, Route } from "svelte-routing";

  import ProtectedRoute from "./lib/protected/ProtectedRoute.svelte";

  import Home from "./pages/home.svelte";
  import Login from "./pages/login.svelte";
  import Logout from "./pages/logout.svelte";

  import KDM from "./pages/kdm/KDM.svelte";

  export let url = "";
</script>

<Router {url}>
  <Route path="/" component={Home}></Route>
  <Route path="/login" component={Login}></Route>
  <Route path="/logout" component={Logout}></Route>
  <Route path="/kdm">
    <ProtectedRoute component={KDM} />
  </Route>
</Router>