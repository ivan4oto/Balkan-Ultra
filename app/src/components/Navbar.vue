<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-container fluid="sm" class="d-flex justify-content-center">
      <b-row>
        <div class="nav-item">
          <b-col>
            <router-link to="/">
              <b-navbar-brand>Home</b-navbar-brand>
            </router-link>
          </b-col>
        </div>

        <div class="nav-item">
          <b-col>
            <router-link to="/Register">
              <b-navbar-brand>Register</b-navbar-brand>
            </router-link>
          </b-col>
        </div>
        <div class="nav-item">
          <b-col>
            <router-link to="/about">
              <b-navbar-brand>Race Info</b-navbar-brand>
            </router-link>
          </b-col>
        </div>
        <div class="nav-item">
          <b-col>
            <router-link to="/about">
              <b-navbar-brand>Results</b-navbar-brand>
            </router-link>
          </b-col>
        </div>
      </b-row>
    </b-container>
  </b-navbar>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.nav-item {
  border-bottom: 3px solid transparent;
}

.nav-item:hover {
  background-color: rgb(77, 77, 83);
  border-bottom-color: rgb(180, 95, 15);
}
</style>
