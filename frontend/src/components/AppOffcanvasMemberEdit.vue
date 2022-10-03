<template>
  <CButton
    color="primary"
    @click="
      () => {
        visibleEnd = !visibleEnd
      }
    "
    >Edit</CButton
  >
  <COffcanvas
    placement="end"
    :visible="visibleEnd"
    @hide="
      () => {
        visibleEnd = !visibleEnd
      }
    "
  >
    <COffcanvasHeader>
      <COffcanvasTitle>Edit Member</COffcanvasTitle>
      <CCloseButton
        class="text-reset"
        @click="
          () => {
            visibleEnd = false
          }
        "
      />
    </COffcanvasHeader>
    <COffcanvasBody>
      {{ this.this_user }}
      <p>-------------------------------------</p>
      <CForm @submit.prevent="submitMember">
        <div class="mb-3">
          <CFormLabel for="name">Name:</CFormLabel>
          <CFormInput
            id="name"
            type="text"
            placeholder="Member Name"
            name="name"
            v-model="this_user.name"
          />
          <!--  -->
        </div>
        <div class="mb-3">
          <CFormLabel for="email"><b>E-mail:</b></CFormLabel>
          <CFormInput
            id="email"
            name="email"
            type="email"
            placeholder="Member Name"
            v-model="this_user.email"
          ></CFormInput>
          <!--  -->
        </div>
        <div>
          <CFormLabel for="role"><b>User Role:</b></CFormLabel>
          <CFormSelect
            aria-label="Assign"
            id="assigned"
            name="assigned"
            v-model="selectedRole"
          >
            <option
              v-for="(roles, index) in userRoles"
              v-bind:key="index"
              v-bind:value="index"
              :selected="this_user.user_role == index"
            >
              {{ roles }}
            </option>
          </CFormSelect>
        </div>
        <hr />
        <CCol :xs="12">
          <CButton color="primary" type="submit">Submit Member</CButton>
          <div class="vr"></div>
          <CButton
            color="secondary"
            type="submit"
            @click.prevent="
              () => {
                visibleEnd = !visibleEnd
              }
            "
            >Cancel
          </CButton>
        </CCol>
      </CForm>
    </COffcanvasBody>
  </COffcanvas>
</template>
<script>
import axios from 'axios'
export default {
  props: ['user'],
  data() {
    return {
      visibleEnd: false,
      this_user: this.user,
      // Store
      userRoles: this.$store.state.userRoles,
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      selectedRole: '',
      // name: '',
      // email: '',
      // user_role: '',
    }
  },
  methods: {
    async submitMember() {
      const user_data = {
        id: this.user.id,
        name: this.user.name,
        email: this.user.email,
        user_role: this.selectedRole,
        // selectedRole: selectedRole,
      }
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      console.log('USER DATA: ', user_data)
      await axios
        .put(`${this.apiURL}/user/` + this.user.id, user_data, { headers })
        .then(
          (response) => console.log('USER: ' + JSON.stringify(response.data)),
          (this.visibleEnd = !this.visibleEnd),
        )
        .catch((error) => console.log(`${error}`))
    },
  },
}
</script>
