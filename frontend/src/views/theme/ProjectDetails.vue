<template>
  <CRow>
    <CCol :xs="12">
      <CCallout color="secondary" class="bg-white">
        <!-- border-top border-top-primary border-end border-end-primary border-bottom border-bottom-primary -->
        <h4>This is Project Overview or Project Title</h4>
        <div class="">
          <dl class="row">
            <dd
              class="col-sm-12 d-flex w-75 justify-content-between align-items-center"
            >
              Create Date :<em class="text-muted"> Sep 12, 2022</em
              ><span class="text-muted">|</span>Due Date :<em
                class="text-muted"
              >
                Dec 29, 2022</em
              ><span class="text-muted">|</span><span>Priority:</span
              ><CBadge color="danger">Critical</CBadge
              ><span class="text-muted">|</span><span>Status:</span
              ><span class="text-success"><em>New</em></span>
            </dd>
          </dl>
        </div>
      </CCallout>
    </CCol>
    <CCol :lg="4">
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>DETAILS</small> </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem
              class="d-flex justify-content-between align-items-center"
            >
              Project No.
              <small>070922-N073</small>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Title</h6>
                <small>Bug in Login and Logout</small>
              </div>
            </CListGroupItem>
            <!-- <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Project</h6>
                <small>Project Title 3</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Type</h6>
                <small class="text-dark">Bug</small>
              </div>
            </CListGroupItem> -->
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Priority</h6>
                <CBadge color="danger">Critical</CBadge>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Status</h6>
                <small class="text-info">In Progress</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Start Date</h6>
                <small>Sep 12, 2022</small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Due Date</h6>
                <small>Dec 29, 2022</small>
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <div class="d-flex w-100 justify-content-between align-items-center">
            <small class="">TEAM MEMBERS</small>
            <span class="text-end"
              ><CButton color="primary" variant="ghost" class="btn-sm"
                >Invite+</CButton
              ></span
            >
          </div>
        </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem>
              <div
                class="d-flex w-100 justify-content-between align-items-center"
              >
                <p class="mb-1">Daniel Canales</p>
                <!-- <CAvatar 
                  size="md" 
                  :src="avatar.src"
                  :status="avatar.status"/>         -->
                <small> <span class="text-muted">UI / UX</span></small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div
                class="d-flex w-100 justify-content-between align-items-center"
              >
                <p class="mb-1">Konstantinos Kakoulis</p>
                <small> <span class="text-muted">Web Developer</span></small>
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div
                class="d-flex w-100 justify-content-between align-items-center"
              >
                <p class="mb-1">Jennifer Walker</p>
                <small>
                  <span class="text-muted">Backend Developer</span></small
                >
              </div>
            </CListGroupItem>
            <CListGroupItem>
              <div
                class="d-flex w-100 justify-content-between align-items-center"
              >
                <p class="mb-1">Tony Brafford</p>
                <small>
                  <span class="text-muted">Frontend Devloper</span></small
                >
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
    </CCol>
    <CCol :lg="8">
      <CCard class="mb-4">
        <CCardHeader> <strong></strong> <small>OVERVIEW</small> </CCardHeader>
        <CCardBody>
          <p class="text-medium-emphasis small">
            It will be as simple as occidental in fact, it will be Occidental.
            To an English person, it will seem like simplified English, as a
            skeptical Cambridge friend of mine told me what Occidental is. The
            European languages are members of the same family. Their separate
            existence is a myth. For science, music, sport, etc, Europe uses the
            same vocabulary. The languages only differ in their grammar, their
            pronunciation and their most common words.
          </p>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <div class="d-flex w-100 justify-content-between align-items-center">
            <small>COMMENTS</small>
            <span class="text-end"
              ><CButton color="primary" variant="ghost" class="btn-sm"
                >Add Comment</CButton
              ></span
            >
          </div>
        </CCardHeader>
        <CCardBody>
          <CCard class="">
            <CCardBody>
              <!-- <CCardTitle>Card title</CCardTitle> w-75-->
              <CCardSubtitle
                >Kakoulis Kostas
                <small class="text-muted"
                  >20 Dec 2021 - 05:47AM</small
                ></CCardSubtitle
              >
              <CCardText>
                <p class="text-medium-emphasis small">
                  I am getting message from customers that when they place order
                  always get error message .
                </p>
                <!-- <p><CCardLink>Edit</CCardLink></p> -->
              </CCardText>
              <!-- <CButton href="#">Go somewhere</CButton> -->
            </CCardBody>
          </CCard>
          <CCard class="">
            <CCardBody>
              <!-- <CCardTitle>Card title</CCardTitle> w-75-->
              <CCardSubtitle
                >Panagiotidou Noula
                <small class="text-muted"
                  >20 Dec 2021 - 05:47AM</small
                ></CCardSubtitle
              >
              <CCardText>
                <p class="text-medium-emphasis small">
                  I am getting message from customers that when they place order
                  always get error message .
                </p>
                <p><CCardLink>Edit</CCardLink></p>
              </CCardText>
              <!-- <CButton href="#">Go somewhere</CButton> -->
            </CCardBody>
          </CCard>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
export default {
  name: 'ProjectDetails',
}
</script>
