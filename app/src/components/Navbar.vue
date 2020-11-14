<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-container fluid="sm" class="d-flex justify-content-center">
      <b-row>
        <b-col>
          <router-link to="/">
            <b-navbar-brand>Home</b-navbar-brand>
          </router-link>
        </b-col>
        <b-col>
          <router-link to="/about">
            <b-navbar-brand>Register</b-navbar-brand>
          </router-link>
        </b-col>
        <b-col>
          <router-link to="/about">
            <b-navbar-brand>Race Info</b-navbar-brand>
          </router-link>
        </b-col>
        <b-col>
          <router-link to="/about">
            <b-navbar-brand>Results</b-navbar-brand>
          </router-link>
        </b-col>
      </b-row>
    </b-container>
  </b-navbar>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped></style>
