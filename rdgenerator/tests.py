from django.test import TestCase

from .api_views import validate_generate_params
from .forms import GenerateForm


class OssRendezvousCompatibilityTests(TestCase):
    def test_form_enables_oss_token_omission_by_default(self):
        self.assertIs(GenerateForm.base_fields['ossRendezvousNoToken'].initial, True)

    def test_api_enables_oss_token_omission_by_default(self):
        cleaned, errors = validate_generate_params({'exename': 'custom-client'})

        self.assertEqual(errors, {})
        self.assertIs(cleaned['delayFix'], True)
        self.assertIs(cleaned['ossRendezvousNoToken'], True)

    def test_api_allows_oss_token_omission_to_be_disabled(self):
        cleaned, errors = validate_generate_params({
            'exename': 'custom-client',
            'ossRendezvousNoToken': False,
        })

        self.assertEqual(errors, {})
        self.assertIs(cleaned['ossRendezvousNoToken'], False)

    def test_api_rejects_non_boolean_oss_setting(self):
        _, errors = validate_generate_params({
            'exename': 'custom-client',
            'ossRendezvousNoToken': 'false',
        })

        self.assertEqual(errors['ossRendezvousNoToken'], 'Must be a boolean value.')
