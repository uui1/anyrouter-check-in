import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from checkin import format_check_in_notification


def test_format_check_in_notification_returns_full_chinese_message():
	detail = {'name': 'Account 1', 'provider': 'anyrouter'}

	message = format_check_in_notification(detail)

	assert '成功账号：Account 1' in message
	assert '✅ 签到成功' in message
	assert '🏷️ 供应商：anyrouter' in message


def test_format_check_in_notification_defaults_provider_when_missing():
	detail = {'name': 'Account 2'}

	message = format_check_in_notification(detail)

	assert '成功账号：Account 2' in message
	assert '🏷️ 供应商：unknown' in message


def test_format_check_in_notification_defaults_account_when_missing():
	detail = {'provider': 'anyrouter'}

	message = format_check_in_notification(detail)

	assert '成功账号：unknown' in message
