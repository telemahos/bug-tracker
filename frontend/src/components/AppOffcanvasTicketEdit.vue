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
    <!-- {{ the_case }} -->
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
          >
            <option v-for="(type_options,index) in case_type_options " :selected="the_case.case_type == index">
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
            v-model="the_case.ticketPriority"
          >
            <option v-for="(priority_option,index) in priority_options " :selected="the_case.priority == index">
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
          >
            <option v-for="(status_option,index) in status_options" :selected="the_case.status == index">
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
          <div class="vr"></div>
          <CButton color="secondary" type="submit">Cancel </CButton>
        </CCol>
      </CForm>
      
    </COffcanvasBody>
  </COffcanvas>
</template>
<script>
export default {
  // inject: ['all_cases'],
  props: ['the_case'],
  data() {
    return {
      the_projects: JSON.parse(this.$store.state.all_projects),
      the_users: JSON.parse(this.$store.state.all_users),
      visibleEnd: false,
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
}
</script>
