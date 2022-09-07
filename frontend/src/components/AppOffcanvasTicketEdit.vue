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
      <COffcanvasTitle>Ticket</COffcanvasTitle>
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
    {{ the_case }}
    <p>-------------------------------------</p>
      <CForm @submit.prevent="submitTicket">
        <div class="mb-3">
          <CFormLabel for="title">Title:</CFormLabel>
          <CFormInput
            id="title"
            type="text"
            placeholder="Ticket Title"
            name="title"
            v-model="the_case.title"
          />
        </div>
        <div class="mb-3">
          <CFormLabel for="description"><b>Description:</b></CFormLabel>
          <CFormTextarea
            id="description"
            rows="3"
            v-model="the_case.description"
          ></CFormTextarea>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketType"><b>Ticket Type:</b></CFormLabel>
          <CFormSelect
            aria-label="Ticket Type"
            id="ticketType"
            name="ticketType"
            v-model="ticketType"
          >
            <option v-for="(type_options,index) in case_type_options " v-bind:key="index" v-bind:value="index"
            :selected="the_case.case_type == index">
              {{ type_options }}
            </option>

            <!-- v-model="the_case.case_type"-->
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketPriority"
            ><b>Ticket Priority:</b></CFormLabel
          >
          <CFormSelect
            aria-label="Ticket Priority"
            id="ticketPriority"
            name="ticketPriority"
            v-model="ticketPriority"
          >
            <!-- v-model="the_case.priority" -->
            <option v-for="(priority_option,index) in priority_options " 
            v-bind:key="index" v-bind:value="index"
            :selected="the_case.priority == index">
              {{ priority_option }}
            </option>
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="ticketStatus"><b>Ticket Status:</b></CFormLabel>
          <CFormSelect
            aria-label="Ticket Status"
            id="ticketStatus"
            name="ticketStatus"
            v-model="ticketStatus"
          >
          <!-- v-model="the_case.status" -->
            <option v-for="(status_option,index) in status_options" 
            v-bind:key="index" v-bind:value="index"
            :selected="the_case.status == index">
              {{ status_option }}
            </option> 
          </CFormSelect>
        </div>
        <div class="mb-3">
          <CFormLabel for="projectSelected"><b>Project:</b></CFormLabel>
          <CFormSelect
            aria-label="Project Selected"
            id="projectSelected"
            name="projectSelected"
            
          >
            <option v-for="(projects ,index) in the_projects" :selected="the_case.project_id === projects.id">
              {{ projects.title }}
            </option> 

            <option
              v-for="project in projects"
              v-bind:key="project.title"
              v-bind:value="project.id"
            >
              {{ project.title }}
            </option>
          </CFormSelect>
        </div> 
        <div class="mb-3">
          <CFormLabel for="assigned"><b>Assign to:</b></CFormLabel>
          <CFormSelect
            aria-label="Assign"
            id="assigned"
            name="assigned"
          >
          <option v-for="(users ,index) in the_users" :selected="the_case.owner_id == users.id">
              {{ users.name }}
            </option> 
          </CFormSelect>
        </div> 
        <hr />
        <CCol :xs="12">
          <CButton color="primary" type="submit">Submit Ticket</CButton>
          <div class="vr"> </div>
          <CButton 
            color="secondary" 
            type="submit"
            @click.prevent="
              () => {
                visibleEnd = !visibleEnd
              }
            "
          >Cancel </CButton>
        </CCol>
      </CForm>
    </COffcanvasBody>
  </COffcanvas>
</template>
<script>
import axios from 'axios'
export default {
  // inject: ['all_cases'],
  props: ['the_case'],
  data() {
    return {
      // Store
      token: this.$store.state.token,
      apiURL: this.$store.state.apiURL,
      
      the_projects: JSON.parse(this.$store.state.all_projects),
      the_users: JSON.parse(this.$store.state.all_users),
      visibleEnd: false,
      today: '',
      due_date: '',
      title: '',
      description: '',
      ticketStatus: '',
      ticketPriority: '',
      ticketType: '',
      projects: [],
      users: [],
      ticketType: '',
      case_type_options: {
        '1': 'Issue',
        '2': 'Bug',
        '3': 'Note'      
      },
      status_options: {
        '1': 'New',
        '2': 'In Progress',
        '3': 'On Hold',
        '4': 'Solved'
      },
      priority_options: {
        '1': 'Normal',
        '2': 'Medium',
        '3': 'High',
        '4': 'Critical'
      }
    }
  },
  methods: {
    async submitTicket() {
      const case_data = {
        id: this.the_case.id,
        today: this.the_case.today,
        due_date: this.the_case.due_date,
        title: this.the_case.title,
        description: this.the_case.description,
        tags: 'test Tag',
        status: this.ticketStatus,
        priority: this.ticketPriority,
        case_type: this.ticketType,
        // project_id: this.projectSelected.value,
        // owner_id: this.assigned.value,
      }
      const headers = {
        Authorization: `Bearer ${this.token}`,
        'Content-Type': 'application/json',
      }
      console.log('TICKET DATA: ', case_data)
      await axios
         .put(`${this.apiURL}/case/` + this.the_case.id, case_data, { headers })
         .then((response) =>
           console.log('New Case: ' + JSON.stringify(response.data)),
         )
         .catch((error) => console.log(`${error}`))
    },
  },
}
</script>
