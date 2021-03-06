import React from 'react';
import { shallow } from 'enzyme';
// import { IntlProvider } from 'react-intl';

import { LandingPage } from '../index';
import LandingPageWrapper from '../LandingPageWrapper';

describe('<LandingPage />', () => {
  it('should render wrapper', () => {
    const renderedComponent = shallow(
      <LandingPage />
    );
    expect(renderedComponent.find(LandingPageWrapper).length).toEqual(1);
  });
});
