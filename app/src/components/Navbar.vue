<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-container>
        <router-link to="/">
          <b-button variant="dark" size="lg">Home</b-button>
        </router-link>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <router-link to="/Register">
              <b-button variant="dark" size="lg">Register</b-button>
            </router-link>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-dropdown variant="dark" size="lg" text="Results">
              <router-link to="Results">
                <a role="menuitem" target="_self" class="dropdown-item">
                  2020
                </a>
              </router-link>
              <b-dropdown-item disabled>2021</b-dropdown-item>
            </b-dropdown>
            <router-link to="/about">
              <b-button variant="dark" size="lg">Race Info</b-button>
            </router-link>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped></style>
