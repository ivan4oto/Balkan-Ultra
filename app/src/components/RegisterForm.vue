<template>
  <div>
    <b-container>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Email address:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Names:" label-for="input-2">
          <b-form-input
            class="mb-2"
            id="input-2"
            v-model="form.firstname"
            required
            placeholder="First name"
          ></b-form-input>

          <b-form-input
            id="input-2"
            class="mb-2"
            v-model="form.secondname"
            required
            placeholder="Second name"
          ></b-form-input>

          <b-form-input
            id="input-2"
            class="mb-2"
            v-model="form.lastname"
            required
            placeholder="Last name"
          ></b-form-input>
        </b-form-group>

        <b-form-row align-h="start">
          <b-col cols="4">
            <b-form-group
              id="input-group-3"
              label="Gender:"
              label-for="input-3"
            >
              <b-form-select
                id="input-3"
                v-model="form.gender"
                :options="genders"
                required
              ></b-form-select>
            </b-form-group>
          </b-col>

          <b-col cols="4">
            <b-form-group
              label="Additional beds:"
              description="Допълнителни легла за спане в хижа Плевен"
            >
              <b-form-input type="number" placeholder="Extra beds">
              </b-form-input>
            </b-form-group>
          </b-col>
        </b-form-row>

        <b-row align-h="start">
          <b-col cols="8">
            <b-form-group
              label="Qualifying Race:"
              description="Моля поставете линк към резултати на състезания доказващи, че нема бедствате по чукарите."
            >
              <b-form-input type="url"></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols='2'>
            <b-button size='sm' variant="outline-primary" class="mb-1">Add Link</b-button>
            <b-button size='sm' variant="outline-danger">Remove Link</b-button>
          </b-col>
        </b-row>

        <!-- 
        <b-form-group id="input-group-4">
          <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
            <b-form-checkbox value="me">Check me out</b-form-checkbox>
            <b-form-checkbox value="that">Check that out</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group> -->

        <b-row class="justify-content-md-center pt-5">
          <b-button type="submit" variant="primary" class="mr-1">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-row>
      </b-form>
      <!-- <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card> -->
    </b-container>
  </div>
</template>

<script>
export default {
  name: "RegisterForm",
  data() {
    return {
      form: {
        email: "",
        firstname: "",
        secondname: "",
        lastname: "",
        gender: null,
        extraBeds: 0,
        checked: [],
      },
      genders: [{ text: "Select One", value: null }, "Male", "Female"],
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.food = null;
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
