<script lang="ts">
  import { Router, Route } from "svelte-routing";

  import ProtectedRoute from "./lib/protected/ProtectedRoute.svelte";

  import Home from "./pages/home.svelte";
  import Login from "./pages/login.svelte";
  import Logout from "./pages/logout.svelte";
  import Signup from "./pages/signup.svelte";
  import About from "./pages/about.svelte";
  import KDM from "./pages/kdm/KDM.svelte";

  export let url = "";
</script>

<Router {url}>
  <Route path="/" component={Home}></Route>
  <Route path="/login" component={Login}></Route>
  <Route path="/logout" component={Logout}></Route>
  <Route path="/signup" component={Signup}></Route>
  <Route path="/about" component={About}></Route>
  <Route path="/kdm">
    <ProtectedRoute component={KDM} />
  </Route>
</Router>
