<template>
  <div>
    <v-container>
      <v-row row>
        <v-col>
          <v-flex>
            <v-text-field label="First Name"></v-text-field>
          </v-flex>
        </v-col>

        <v-col>
          <v-flex>
            <v-text-field label="Second Name"></v-text-field>
          </v-flex>
        </v-col>

        <v-col>
          <v-flex>
            <v-text-field label="Third Name"></v-text-field>
          </v-flex>
        </v-col>
      </v-row>

      <v-row row>
        <v-col cols="2">
          <v-flex>
            <v-radio-group v-model="radioGroup" mandatory>
              <v-radio label="Male" value="radio-1"></v-radio>
              <v-radio label="Female" value="radio-2"></v-radio>
            </v-radio-group>
          </v-flex>
        </v-col>
        <v-col cols="4">
          <v-flex>
            <v-text-field label="Email"></v-text-field>
          </v-flex>
        </v-col>
        <v-col cols="6">
          <v-flex>
            <v-text-field label="Phone Number"></v-text-field>
          </v-flex>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  data: () => ({
    radioGroup: null,
    rules: [
      (value) => !!value || "Required.",
      (value) => (value && value.length >= 3) || "Min 3 characters",
    ],
  }),
};
</script>
