<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-container fluid="sm" class="d-flex justify-content-center">
      <b-row>
        <div class="nav-item">
          <b-col>
            <router-link to="/">
              <b-button variant="dark" size='lg'>Home</b-button>
            </router-link>
          </b-col>
        </div>

        <div class="nav-item">
          <b-col>
            <router-link to="/Register">
              <b-button variant="dark" size='lg'>Register</b-button>
            </router-link>
          </b-col>
        </div>
        <div class="nav-item">
          <b-col>
            <router-link to="/about">
              <b-button variant="dark" size='lg'>Race Info</b-button>
            </router-link>
          </b-col>
        </div>
        <b-col>
          <b-dropdown variant="dark" size="lg" text="Results">
            <b-dropdown-item>2019</b-dropdown-item>
            <b-dropdown-item disabled>2020</b-dropdown-item>
          </b-dropdown>
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

<style scoped>

</style>
