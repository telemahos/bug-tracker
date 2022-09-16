<template>
  <h1>Project New</h1>

  <CRow>
    <CCol :xs="12">
      <CCard class="mb-4">
        <CCardHeader>
          <strong>Create a Project</strong>
        </CCardHeader>
        <CCardBody>
          <CForm @submit.prevent="submitProject">
            <div class="mb-3 form-floating">
              <CFormLabel for="title"><b>Title:</b></CFormLabel>
              <CFormInput
                id="title"
                type="text"
                floatingLabel="Project Title"
                placeholder="Project Title"
                name="title"
                v-model="title"
              />
            </div>
            <div class="mb-3 form-floating">
              <CFormTextarea
                id="description"
                floatingLabel="Description"
                placeholder="Description"
                rows="3"
                style="height: 100px"
                v-model="description"
              ></CFormTextarea>
              <!-- <CFormLabel for="description"><b>Description:</b></CFormLabel> -->
            </div>
            <!-- Today and Due Date -->
            <div class="mb-3 form-check-inline">
              <label for="startDate">Start Date</label>
              <flat-pickr
                id="startDate"
                type="text"
                class="form-control"
                placeholder="startDate"
                name="startDate"
                v-model="startDate"
                :config="config"
              >
              </flat-pickr>
            </div>
            <div class="mb-3 form-check-inline">
              <label for="duedate">Due Date</label>
              <flat-pickr
                v-model="duedate"
                :config="config"
                class="form-control"
                placeholder="Due Date"
                name="duedate"
              >
              </flat-pickr>
            </div>
            <!--<div class="mb-3">
              <CFormLabel for="projectActive"
                ><b>Is Active:</b></CFormLabel
              >
              <CFormSelect
                aria-label="Project Active"
                id="projectActive"
                name="projectActive"
                v-model="projectActive"
              >                
                <option value="1">Yes</option>
                <option value="2">No</option>
              </CFormSelect>
            </div> -->
            <div class="mb-3">
              <CFormLabel for="projectStatus"
                ><b>Project Status:</b></CFormLabel
              >
              <CFormSelect
                aria-label="Project Status"
                id="projectStatus"
                name="projectStatus"
                v-model="projectStatus"
              >
                <option value="1">New</option>
                <option value="2">In Progress</option>
                <option value="3">On Hold</option>
                <option value="4">Solved</option>
              </CFormSelect>
            </div>
            <div class="mb-3">
              <CFormLabel for="projectPriority"
                ><b>Project Priority:</b></CFormLabel
              >
              <CFormSelect
                aria-label="Project Priority"
                id="projectPriority"
                name="projectPriority"
                v-model="projectPriority"
              >
                <option selected disabled>Priority</option>
                <option value="1">Normal</option>
                <option value="2">Medium</option>
                <option value="3">High</option>
                <option value="4">Critical</option>
              </CFormSelect>
            </div>

            <div class="mb-3">
              <CFormLabel for="team"
                ><b>Team:</b></CFormLabel
              >
              <!-- name="team"
                id="team" trackBy= 'role' label="label" :object="true" :searchable="true" -->
              <Multiselect
                v-model="value"
                placeholder="Choose your team"
                mode="tags"
                trackBy= 'value'
                label= "label"
                :close-on-select="false"
                :create-option="true"
                :options= "allUsers"
              />
            </div>

            <p>VALUE: {{ value }}</p>

            <hr />
            <CCol :xs="12">
              <CButton color="primary" type="submit">Submit Project</CButton>
              <div class="vr"></div>
              <CButton color="secondary" type="submit">Cancel </CButton>
            </CCol>
          </CForm>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
import axios from 'axios'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'
import 'vue-multiselect/dist/vue-multiselect.min.css'
import Multiselect from '@vueform/multiselect'

export default {
  name: 'ProjectNew',
  components: {
    flatPickr,
    Multiselect,
  },
  data() {
    return {
      value: null,
      options: [
        'Batman',
        'Robin',
        'Joker',
      ],
      duedate: '',
      startDate: '',
      today: this.$store.state.today,
      year: '',
      month: '',
      day: '',
      config: {
        wrap: true, // set wrap to true only when using 'input-group'
        altFormat: 'd-m-Y',
        altInput: true,
        dateFormat: 'Y-m-d',
      },
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      title: '',
      description: '',
      active: '1',
      projectStatus: '',
      projectPriority: '',
      team_id: '',
      owner_id: '',
      allUsers: [],
      theUser: {},
    }
  },
  mounted() {
    this.year = this.today.getFullYear()
    this.day = this.today.getDate()
    this.month = this.today.getMonth() + 1

    console.log('TODAY:', this.day + '-' + this.month + '-' + this.year)

    if (parseInt(this.month) <= 9) {
      this.month = '0' + this.month
    }
    if (parseInt(this.day) <= 9) {
      this.day = '0' + this.day
    }
    this.today = this.day + '-' + this.month + '-' + this.year

    const headers = {
      Authorization: `Bearer ${this.token}`,
      'Content-Type': 'application/json',
    }
    axios
      .get(`${this.apiURL}/user`, { headers })
      .then((response) => {
        this.users = response.data
        this.getUsers()
      })
      .catch((error) => console.log(`${error}`))
  },
  methods: {
    getUsers() {
      for (let i = 0; i < this.users.length; i++) {
        this.theUser[i] = { value: this.users[i].id, label: this.users[i].name }
        this.allUsers[i] = this.theUser[i]
      }
    }
  },
}
</script>

<style src="@vueform/multiselect/themes/default.css"></style>