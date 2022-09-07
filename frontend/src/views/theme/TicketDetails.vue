<template>
  <h1>This is ticket details page! <small class="text-muted">Bug in Login and Logout</small> </h1>

  <CRow>
    <CCol :xs="12">
      <!-- <DocsCallout name="Badges" href="components/badge.html" />-->
    </CCol>
    <CCol :lg="4">
      <CCard class="mb-4">
        <CCardHeader>
          <strong></strong> <small>DETAILS</small>
        </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem
            class="d-flex justify-content-between align-items-center"
            >
            Case No.
                <small>070922-N073</small>
            </CListGroupItem>
            <CListGroupItem>
                <div class="d-flex w-100 justify-content-between">
                  <h6 class="mb-1">Title</h6>
                  <small>Bug in Login and Logout</small>
                </div>
            </CListGroupItem>
            <CListGroupItem>
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
            </CListGroupItem>
            <CListGroupItem>
                <div class="d-flex w-100 justify-content-between">
                  <h6 class="mb-1">Priority</h6>
                  <CBadge color="danger">Critical</CBadge>
                </div>
            </CListGroupItem>
            <CListGroupItem>
                <div class="d-flex w-100 justify-content-between">
                  <h6 class="mb-1">Status</h6>
                  <small  class="text-info">In Progress</small>
                </div>
            </CListGroupItem>
            <CListGroupItem>
                <div class="d-flex w-100 justify-content-between">
                  <h6 class="mb-1">Due Date</h6>
                  <small>Sep 28, 2022</small>
                </div>
            </CListGroupItem>
          </CListGroup>
            
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <strong></strong> <small>ASSIGNED TO</small>
        </CCardHeader>
        <CCardBody>
          <CListGroup>
            <CListGroupItem>
              <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">Owner</h6> 
                <!-- <CAvatar 
                  size="md" 
                  :src="avatar.src"
                  :status="avatar.status"/>         -->      
                <small> Konstantinos Kakoulis<br><span class="text-muted">Web Devloper</span></small>
              </div>
            </CListGroupItem>
          </CListGroup>
        </CCardBody>
      </CCard>
    </CCol>
    <CCol :lg="8">
      <CCard class="mb-4">
        <CCardHeader>
          <strong></strong> <small>DESCRIPTION</small>
        </CCardHeader>
        <CCardBody>
          <p class="text-medium-emphasis small">
            It will be as simple as occidental in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is. The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.
          </p>
        </CCardBody>
      </CCard>
      <CCard class="mb-4">
        <CCardHeader>
          <strong></strong> <small>COMMENTS</small>
        </CCardHeader>
        <CCardBody>
          <p class="text-medium-emphasis small">
            Apply the <code>shape=&#34;rounded-pill&#34;</code> prop to make
            badges rounded.
          </p>
          <DocsExample href="components/badge.html#pill-badges">
            <CBadge color="primary" shape="rounded-pill"> primary </CBadge>
            <CBadge color="success" shape="rounded-pill"> success </CBadge>
            <CBadge color="danger" shape="rounded-pill"> danger </CBadge>
            <CBadge color="warning" shape="rounded-pill"> warning </CBadge>
            <CBadge color="info" shape="rounded-pill"> info </CBadge>
            <CBadge color="light" shape="rounded-pill"> light </CBadge>
            <CBadge color="dark" shape="rounded-pill"> dark </CBadge>
          </DocsExample>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
import avatar from '@/assets/images/avatars/2.jpg'
export default {
  name: 'ticketdetails',
  setup() {
    return {
      // avatar: avatar,
      avatar: { src: avatar, status: 'success' },
    }
  },
}
</script>