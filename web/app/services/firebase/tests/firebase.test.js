// import axios from 'axios';
// import rewire from 'rewire';
import moxios from 'moxios';
import sinon from 'sinon';
import {
  parseResults,
  checkStatus,
  getFoodProfile,
  getMultiFoodProfile } from '../firebase';
import {
  getFoodProfileMockSuccess,
  getMultiFoodProfileMockSuccess } from '../../../mocks/getFoodProfileMock';

describe('firebase', () => {
  beforeEach(() => {
    moxios.install();
  });
  afterEach(() => {
    moxios.uninstall();
  });
  it('getFoodProfile', (done) => {
    const payload = getFoodProfileMockSuccess;
    const onFulfilled = sinon.spy();
    getFoodProfile('02049').then(onFulfilled);
    moxios.wait(() => {
      const request = moxios.requests.mostRecent();
      // Override with a mocked response via a specified payload.
      request.respondWith(payload).then(() => {
        expect(onFulfilled.getCall(0).args[0].SN).toBe('02049');
        expect(onFulfilled.getCall(0).args[0].name).toBe(getFoodProfileMockSuccess.response.name);
        done();
      });
    });
  });
  it('getMultiFoodProfile', (done) => {
    // const payload = getMultiFoodProfileMockSuccess;
    const onFulfilled = sinon.spy();
    moxios.stubRequest(/.*profiles\/00000.json.*/, getMultiFoodProfileMockSuccess[0]);
    moxios.stubRequest(/.*profiles\/00001.json.*/, getMultiFoodProfileMockSuccess[1]);
    getMultiFoodProfile(['00000', '00001']).then(onFulfilled);
    // moxios wait for stubs complete etc.
    moxios.wait(() => {
      expect(onFulfilled.getCall(0).args[0]['00000']).toMatchObject(getMultiFoodProfileMockSuccess[0].response);
      expect(onFulfilled.getCall(0).args[0]['00001']).toMatchObject(getMultiFoodProfileMockSuccess[1].response);
      done();
    });
  });
  it('parseResults', (done) => {
    const responseSuccess = { status: 200, data: { a: 'a', b: 'b', c: 'c' } };
    const responseFailure = { status: 404 };
    expect(parseResults(responseSuccess)).toMatchObject(responseSuccess.data);
    expect(parseResults(responseFailure)).toBe(null);
    done();
  });
  it('checkStatus', (done) => {
    const responseSuccess = { status: 200, data: { a: 'a', b: 'b', c: 'c' } };
    const responseFailure = { status: 404 };
    expect(checkStatus(responseSuccess)).toMatchObject(responseSuccess);
    expect(() => { checkStatus(responseFailure); }).toThrow();
    done();
  });
});
